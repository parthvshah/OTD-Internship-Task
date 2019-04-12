# OTD-Internship-Task
The preliminary for IIIT Delhi Summer Internship, 2019

## Approach
A 2D matrix holds information about all the routes and stops on these routes. This is done by assigning a row in this for each unique route. Each column is assigned a unique stop.
If a stop (column) exists on a particular route (row), it is indicated by it's stop sequence, an integer. If the stop does not exist on a particular route, it holds ```-1```.

For example, if route ```0``` has stops ```0,3``` and route ```1``` has ```0,2,3``` in those particular orders, the array would look like this.

```
[[0, -1, -1, 1, -1]
 [0, -1, 1, 2, -1]]
```

To find information about a zero stop route, we query the particular row with the source stop. We check if the column corresponding to the destination is not ```-1```. This gives us a zero stop route.
To find information about a one stop route, all possible combinations of routes which have source stop in one route, destination stop in another and with one common stop are generated. This is obtained by iterating through the routes to find combinations and then the stops to find a common stop for each combination. THis gives us a one stop route.

## Run
To run the flask server:
 ```python3 app.py```
