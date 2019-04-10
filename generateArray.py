import math
import csv

no_cols = 3601+1 # Number of stops (3465)
no_rows = 525+1  # Number of routes (543)

rows = []

array = [[-1 for x in range(no_cols)] for y in range(no_rows)]

with open('unique_routes_id.csv', 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
      
    fields = next(csvreader) 
  
    for row in csvreader: 
        rows.append(row) 
  
    # print("Total no. of rows: %d"%(csvreader.line_num))
    # print('Field names are:' + ', '.join(field for field in fields))
    error_count = 0
    exists_count = 0
    for row in rows:
        trip_id = int(row[0].strip())
        stop_id = int(row[1].strip())
        stop = int(row[2].strip())
        
        try:
            if(array[trip_id][stop_id]!=-1):
                print("Error: Exists", trip_id, stop_id, stop)
                exists_count += 1
            else:
                array[trip_id][stop_id] = stop
        except IndexError:
            print("Error: ", trip_id, stop_id)
            error_count += 1
    print(error_count, exists_count)
    
    
    # for i in range(no_rows):
    #     for j in range(no_cols):
    #         print(array[i][j], " ",end="")
    #     print("\n")