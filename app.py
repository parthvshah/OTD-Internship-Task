import csv
from flask import Flask, render_template, request
app = Flask(__name__)

no_cols = 3601+1 # Number of stops (3465)
no_rows = 525+1  # Number of routes (543)

array = [[-1 for x in range(no_cols)] for y in range(no_rows)]

def generateArray():
   print("[Info] Generating array...")
   rows = []

   with open('unique_routes_id.csv', 'r') as csvfile: 
      csvreader = csv.reader(csvfile)
      
      fields = next(csvreader) 

      for row in csvreader: 
         rows.append(row) 

      error_count = 0
      exists_count = 0
      for row in rows:
         trip_id = int(row[0].strip())
         stop_id = int(row[1].strip())
         stop = int(row[2].strip())
         
         try:
            if(array[trip_id][stop_id]!=-1):
                  # print("Error: Exists", trip_id, stop_id, stop)
                  exists_count += 1
            else:
                  array[trip_id][stop_id] = stop
         except IndexError:
            # print("Error: ", trip_id, stop_id)
            error_count += 1
      # print(error_count, exists_count)
      print("[Info] Array generated.")

def generateStops():
   print("[Info] Generating Stops...")
   print("[Info] Stops generated.")

def decodeStops(route_stop):
   pass

def zero_hop(source_id, dest_id):
   possible_routes = []
   route_exists = False

   # if(source_id >= no_cols or source_id <= no_cols or dest_id >= no_cols or dest_id <= no_cols):
   #    return False

   for i in range(no_rows):
      route = array[i]
      if(route[source_id] != -1 and route[dest_id] != -1):
         possible_routes.append([i, route[source_id], route[dest_id]])
         route_exists = True

   if(route_exists):
      print(possible_routes)
      return(possible_routes)
   else:
      print(route_exists)
      return route_exists


def one_hop(source_id, dest_id):
   possible_routes = []
   route_exists = False

   # if(source_id >= no_cols or source_id <= no_cols or dest_id >= no_cols or dest_id <= no_cols):
   #    return False

   source_route = False
   dest_route = False
   for i in range(no_rows):
      route = array[i]
      if(route[source_id] != -1):
         source_route = [i, route[source_id], route]
      if(route[dest_id] != -1):
         dest_route = [i, route[dest_id], route]
   
   if(source_route == False or dest_route == False):
      return False
   else:
      route_exists = True

   source_common_stop = 0
   dest_common_stop = 0
   for j in range(no_cols):
      if(source_route[2][j] != -1 and dest_route[2][j] != -1):
         source_common_stop = source_route[2][j]
         dest_common_stop = dest_route[2][j]
   
   source_route[2] = source_common_stop
   dest_route[2] = dest_common_stop


   if(route_exists):
      print([source_route, dest_route])
      return [source_route, dest_route]
   else:
      print(route_exists)
      return route_exists

def createResult(possible_routes):
   resultArray = []
   for route in possible_routes:
      resultArray.append("Route: "+str(route[0])+" Value: "+str(route[1])+" "+str(route[2]))
   return resultArray

@app.route('/',methods = ['POST', 'GET'])
def query():
   if request.method == 'POST':
      source_id = int(request.form['source_id'])
      dest_id = int(request.form['dest_id'])

      zero_result = zero_hop(source_id, dest_id)
      one_result = one_hop(source_id, dest_id)


      if(zero_result==False):
         zero_result = ['There are no 0 hop routes for given source and destination.']
      else:
         zero_result = createResult(zero_result)
      if(one_result==False):
         one_result = ['There are no 1 hop routes for given source and destination.']
      else:
         one_result = createResult(one_result)
      

      return render_template("query.html", zero_result=zero_result, one_result=one_result)
   else:
      return render_template("query.html")
   return render_template("query.html")

if __name__ == '__main__':
   generateArray()
   generateStops()
   app.run()