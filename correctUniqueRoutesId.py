import csv

rows = []
with open('unique_routes_id.csv', 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        fields = next(csvreader) 
    
        for row in csvreader: 
            rows.append(row) 
    
        for row in rows: 
            route_id = row[0]
            stop_id = row[1]
            stop_seq = row[2]
            
            