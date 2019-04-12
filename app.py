import csv
from flask import Flask, render_template, request
app = Flask(__name__)

no_cols = 3601+1 # Number of stops (3465)
no_rows = 525+1  # Number of routes (543)
no_stops = 3601+1

array = [[-1 for x in range(no_cols)] for y in range(no_rows)]
stops = ["-1" for _ in range(no_stops)]

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
   rows = []

   with open('stops.csv', 'r') as csvfile: 
      csvreader = csv.reader(csvfile)
      
      fields = next(csvreader) 

      for row in csvreader: 
         rows.append(row) 

      exists_count = 0
      error_count = 0
      for row in rows:
         stop_id = int(row[0])
         name = row[2].strip()

         try:
            if(stops[stop_id]!="-1"):
                  # print("Error: Exists", name)
                  exists_count += 1
            else:
                  stops[stop_id] = name
         except IndexError:
            # print("Error: ", stop_id, name)
            error_count += 1
      # print(error_count, exists_count)


   print("[Info] Stops generated.")


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

def find_route_pairs(source_id, dest_id):
   possible_pairs = []

   for i in range(no_rows):
      for ii in range(i,no_rows):
         if(array[i][source_id]!=-1 and array[ii][dest_id]!=-1 and i != ii):
            possible_pairs.append([i, ii])

   if(len(possible_pairs)!=0):
      # print(possible_pairs)
      return possible_pairs
   else:
      # print("False")
      return False


def find_common_route_pairs(possible_pairs):
   common_pairs = []

   for pair in possible_pairs:
      source_route_id = pair[0]
      dest_route_id = pair[1]

      for j in range(no_stops):
         if(array[source_route_id][j]!=-1 and array[dest_route_id][j]!=-1):
            common_pairs.append([source_route_id,dest_route_id,j])
               

   if(len(common_pairs)!=0):
      # print(common_pairs)
      return common_pairs
   else:
      # print("False")
      return False

def find_seq_common_route_pairs(unique_pairs, source_id, dest_id):
   seq_pairs = []

   for pair in unique_pairs:
      source_route_id = pair[0]
      dest_route_id = pair[1]
      common_stop_id = pair[2]

      stop_seq1 = array[source_route_id][source_id]
      stop_seq2 = array[source_route_id][common_stop_id]
      stop_seq3 = array[dest_route_id][common_stop_id]
      stop_seq4 = array[dest_route_id][dest_id]

      if(stop_seq1 <= stop_seq2 and stop_seq3 <= stop_seq4):
         seq_pairs.append([source_route_id, dest_route_id, (stop_seq1, stop_seq2, stop_seq3, stop_seq4)])

      

   if(len(seq_pairs)!=0):
      # print(seq_pairs)
      return seq_pairs
   else:
      # print("False")
      return False


def one_hop(source_id, dest_id):
   possible_routes = []
   route_exists = False

   pairs = find_route_pairs(source_id, dest_id)
   if(pairs == False):
      return False
   unique_pairs = find_common_route_pairs(pairs)
   if(unique_pairs == False):
      return False
   seq_pairs = find_seq_common_route_pairs(unique_pairs, source_id, dest_id)
   if(seq_pairs == False):
      return False

   route_exists = True
   if(route_exists):
      print(seq_pairs)
      return seq_pairs
   else:
      # print("False")
      return False


def createZeroResult(possible_routes):
   resultArray = []
   stop_str = ""
   for route in possible_routes:
      route_id = route[0]
      val1 = route[1]
      val2 = route[2]

      if(val1>val2):
         stop_seq = range(val1,val2-1,-1)
      else:
         stop_seq = range(val1, val2+1, 1)
         
      
      for stop_val in stop_seq:
         for i in range(no_cols):
            if(array[route_id][i]==stop_val):
               stop_str += stops[i] + "\n"
      

      resultArray.append("Route ID: "+str(route_id)+" \nSequence: "+stop_str)
      stop_str = ""

   return resultArray

def createOneResult(possible_routes):
   resultArray = []
   source_stop_str = ""
   dest_stop_str = ""

   for route in possible_routes:
      source_route_id = route[0]
      dest_route_id = route[1]
      stop_seq1 = route[2][0]
      stop_seq2 = route[2][1]
      stop_seq3 = route[2][2]
      stop_seq4 = route[2][3]

      
      source_stop_seq = range(stop_seq1, stop_seq2+1, 1)
      dest_stop_seq = range(stop_seq3, stop_seq4+1, 1)
      
      for stop_val1 in source_stop_seq:
         for i in range(no_cols):
            if(array[source_route_id][i]==stop_val1):
               source_stop_str += stops[i] + "\n"
      

      resultArray.append("Route ID: "+str(source_route_id)+" \nSequence: "+source_stop_str)
      source_stop_str = ""

      for stop_val2 in dest_stop_seq:
         for j in range(no_cols):
            if(array[dest_route_id][j]==stop_val2):
               dest_stop_str += stops[j] + "\n"
      

      resultArray.append("Route ID: "+str(dest_route_id)+" \nSequence: "+dest_stop_str)
      dest_stop_str = ""

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
         zero_result = createZeroResult(zero_result)
      if(one_result==False):
         one_result = ['There are no 1 hop routes for given source and destination.']
      else:
         one_result = createOneResult(one_result)
      

      return render_template("query.html", zero_result=zero_result, one_result=one_result)
   else:
      return render_template("query.html")
   return render_template("query.html")

@app.route('/id')
def id():
   return render_template("id.html")

if __name__ == '__main__':
   generateArray()
   generateStops()
   app.run()