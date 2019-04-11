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
To find information about a one stop route, we query a particular row with the source stop. We then check sequentially for a route that have the destination stop. These source, destination pairs of routes can be used to find the sequence of stops required for transit. This is achieved by iterating through the two obtained routes and looking for a common stop. Then a sequence of stops is built on each route.

## Run
To run the flask server:
 ```python3 app.py```
