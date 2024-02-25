from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import json



def find_letter_links(url):
    driver.get(url)
    driver.maximize_window()
    time.sleep(8)

    pagination = driver.find_element(By.XPATH, '//nav[@class="m-nav--buttons"]')
    arr = []
    pages = pagination.find_elements(By.XPATH, './/a[contains(@class,"m-nav--buttons__item")]')
    print(len(pages))
    for page in pages:  ### skloni rang kad zavsis
        l_link = page.get_attribute("href")
        arr.append(l_link)
        time.sleep(4)
        print(l_link)
    return(arr)




def find_agent_links(l_link):
    #Ulazni parametar je l_link (letter link) -link koji se nalazi u adresi kada se pritisne neko od slova na sajtu
    #Svaki taj link (svako slovo, odgovara agentima koji su prikazani posle pritiska na slovo
    #Linkovi pojedinacnih agenata skladiste se u arr listu koja se isporucuje kao izlazni parametar i dodaje
    #na ostalae abent_linkove u glavnoj proceduri
    driver.get(l_link)
    #container = driver.find_element(By.XPATH, './/div[@class="row"]')
    time.sleep(2)
    agents = driver.find_elements(By.XPATH, './/div[@class="m-person--withimage__image"]')
    time.sleep(2)
    print(len(agents))
    arr = []
    for agent in agents:
        elem = agent.find_element(By.TAG_NAME, 'a')
        a_link = elem.get_attribute('href')
        arr.append(a_link)
        # elem.click()
        print(a_link)
    return(arr)



def get_agent_data(url):
    driver.get(link)
    time.sleep(3)

    container = driver.find_element(By.XPATH, '//div[@class="row"]')

    try:
        pict = container.find_element(By.XPATH, '//img[@class="lazy loaded"]')
        time.sleep(4)
        p_link = pict.get_attribute("src")
    except:
        p_link = "src-??"
    print(p_link)
    name = driver.find_element(By.XPATH, './/h1').text
    time.sleep(2)
    print(name)
    paragraphs = driver.find_elements(By.XPATH, './/p[contains(@class,"e-text")]')
    print(len(paragraphs))
    try:
        position_list = paragraphs[0].text
        position_list = position_list.split('\n')
        position = position_list[-1]
        print(position)
        bereich_list = paragraphs[1].text
        bereich_list = bereich_list.split('\n')
        bereich=bereich_list[-1]
        print(bereich)
    except:
        position = '?????'
        bereich = '?????'
    standort = paragraphs[2].text
    phone_list = standort.split('\n')
    phone = phone_list[-1]
    print(phone)
    dict = {
    'name' : name,
    'position' : position,
    'bereich' : bereich,
    'phone' : phone,
    'p_link' : p_link,
    'url' : url }
    return(dict)



web = "https://www.reutlingen.ihk.de/ansprechpartner/person"
path = "C:/Users/38163/PycharmProjects/ChDriver/chromedriver.exe"

service_path = Service(path)
driver = webdriver.Chrome(service = service_path)


# 1.recording of letter links
letter_links = []
letter_links += find_letter_links(web)

# 2. recording of agent links
agent_links = []
for link in letter_links: ### skloni rang kad zavrsis
     agent_links += find_agent_links(link)

print(len(agent_links))

# 3. recording of agent data
data = []

for link in agent_links: ### skloni rang kad zavrsis
    dict_ag = get_agent_data(link)
    try:
        data.append(dict_ag)
    except:
        print("GRESKA")
        dict_alter =  {'position' : '?????',
                       'bereich' : '?????'}
        dict_ag.update(dict_alter)
        data.append(dict_ag)

# 4. making json file
with open('agents.json', 'w', encoding='utf-8') as json_file:
    json.dump( data, json_file,ensure_ascii=False ,indent=4)




