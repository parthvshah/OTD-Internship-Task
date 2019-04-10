import math
import csv

filename = "stop_times.csv"
  
fields = [] 
rows = []

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    fields = next(csvreader) 
  
    for row in csvreader: 
        rows.append(row) 
  
    print("Total no. of rows: %d"%(csvreader.line_num))
    print('Field names are:' + ', '.join(field for field in fields))
    for row in rows: 
        print(row[0],", ", row[3], ", ",row[4],sep="")
