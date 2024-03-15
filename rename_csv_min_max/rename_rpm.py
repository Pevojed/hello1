import os
import shutil
import pandas as pd
from datetime import datetime

def rename_and_copy(file_path, output_folder):
    # Ucitavanje CSV fajla
    data = pd.read_csv(file_path)

    # Pronalazenje minimalne i maksimalne vrednosti u koloni "Engine Speed (rpm)"
    min_speed = int(round(data['Engine Speed (rpm)'].min()/100,0))
    max_speed = int(round(data['Engine Speed (rpm)'].max()/100,0))

    # Izdvajanje datuma i vremena iz imena fajla
    filename = os.path.basename(file_path)
    filename_no_ext, ext = os.path.splitext(filename)
    date_time_str = filename_no_ext.split('-')
    print(date_time_str)
    date = date_time_str[1].replace('_', '')
    time = date_time_str[2].replace('_', '')
    print(f"{date}, {time}")

    # Generisanje novog imena fajla
    new_filename = f"{date_time_str[0]}_{date}_{time}_{min_speed}-{max_speed}CRPM{ext}"

    # Putanja do novog fajla
    new_file_path = os.path.join(output_folder, new_filename)

    # Kopiranje i preimenovanje fajla
    shutil.copyfile(file_path, new_file_path)


# Putanja do ulaznog foldera
input_folder = 'in'
# Putanja do izlaznog foldera
output_folder = 'out'

# Procesiranje svih fajlova u ulaznom folderu
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        rename_and_copy(file_path, output_folder)