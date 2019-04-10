import math
import csv

route_id_arr = []
trip_id_arr = []

def create_rt_arr():
    fields = [] 
    rows = []
    with open('trips.csv', 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        fields = next(csvreader) 
    
        for row in csvreader: 
            rows.append(row) 
    
        print('Field names are:' + ', '.join(field for field in fields))
        for row in rows: 
            route_id = row[0]
            trip_id = row[2]
            if(route_id not in route_id_arr):
                route_id_arr.append(route_id)
                trip_id_arr.append(trip_id)
        
        # for i in range(len(route_id_arr)):
        #     print(route_id_arr[i], ", ", trip_id_arr[i], sep="")

def create_rs_arr():
    fields = [] 
    rows = []
    with open('all_stops.csv', 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        
        fields = next(csvreader) 
    
        for row in csvreader: 
            rows.append(row) 
    
        print('Field names are:' + ', '.join(field for field in fields))

        for row in rows:
            trip_id = row[0]
            stop_id = row[1]
            stop_sequence = row[2]
            if(trip_id in trip_id_arr):
                print(trip_id, ", ", stop_id, ", ",stop_sequence, sep="")
    
if __name__ == "__main__":
    create_rt_arr()
    create_rs_arr()



