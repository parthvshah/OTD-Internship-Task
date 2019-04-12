import csv
rows = []
with open('stops.csv', 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        fields = next(csvreader) 
    
        for row in csvreader: 
            rows.append(row) 
    
        print('Field names are:' + ', '.join(field for field in fields))
        for row in rows: 
            stop_id = row[0]
            stop_name = row[2]
            
            print("<option value=\"",stop_id,"\">",stop_name,"</option>",sep="")