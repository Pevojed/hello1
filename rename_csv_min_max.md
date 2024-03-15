# Write a script to rename CSV files based on minimums and maximums  
  
I have a number of CSVs like the attached. I would like a script that will  
a) find the "column" that contains "RPM";  
b) finds the minimum and maximum values in that column; and  
c) renames the file by  
1. taking out the _ in the date and the time; and  
2. replacing the - with _; and  
3. appending  
a. "_"  
b. the minimum and maximum RPM values, divided by 100 and rounded, and  
c. "CRPM"  
to the end of the filename before the extension. 
So, for example, the  file the file with name  
simonstools-2024_03_14-05_18_41.csv would be renamed to  
simostools_20240314_051841_25-38CRPM.csv  
In column 'Engine Speed (rpm)' minimal rpm is 2470 and maximal rpm is 3807  