# Create Python Script - Excel Data Extraction


1) find XLSX in local directory - same as python script - must run on Windows  
2) Find data in Sheets; NORAM, LATAM, EMEA, APAC, Columns A through C.  
Where a row has data in columns A through C, find the value in two rows below (planned orders) in find the value in columns E through T.   
3) Copy the value and corresponding month from above column to sheet Data as a new row.   
4) Add the year from row 1 above the cell with month data and to column "Year" in the new sheet.  
5) Where a row has data in columns A through C, copy the data from column V to column "notes" in the new sheet.  
6) Repeat for each instance of  a cell found with data in columns E through T.  
7) Do not copy data if the value is 0  
8) Export to XLSX file in local directory using source XLSX file name + "consolidated_%date%"  
9) Log output to log.txt  in local directory  

[Source file = Forecast_30NOV23.xlsx](/excel_data_extraction/Forecast_30NOV23.xlsx)  
Screenshoot 
![Screenshoot](/excel_data_extraction/Forecast_30NOV23.jpg)  
[Desired Output = Template.xlsx](/excel_data_extraction/Template.xlsx)    
Screenshoot  
![Screenshoot](/excel_data_extraction/considered_planed_orders_with_exclusion.jpg)