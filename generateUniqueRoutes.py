import math
import csv

filename = "unique_routes.csv"
  
fields = [] 
rows = []

trip_id_arr = []

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    fields = next(csvreader) 
  
    for row in csvreader: 
        rows.append(row) 
  
    # print("Total no. of rows: %d"%(csvreader.line_num))
    # print('Field names are:' + ', '.join(field for field in fields))

    for row in rows:
        trip_id = row[0]
        if(trip_id not in trip_id_arr):
            trip_id_arr.append(int(trip_id.strip()))

    print(len(trip_id_arr))
    
    count = -1
    for row in rows:
        trip_id = int(row[0].strip())
        stop_id = int(row[1].strip())
        stop = int(row[2].strip())
        if(stop==0):
            count += 1
        print(count, ", ", stop_id, ", ", stop, sep="")
    