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

    for row in rows: 
        print(row[0],", ", row[3], ", ",row[4],sep="")
