# Anomalies
Documentation for the anomalies in the given dataset.

## Stop Sequence
The stop sequenece given as part of the stop_times.txt file had sequencing errors. New routes started with 0 but there were missing numbers in the stop sequence. This was corrected. Example: Route 327, missing 19.

## Stop ID
There are multiple stops with same names (or extremely similar names, difference being a space) which have different ID's. Example: Haidarpur Water Works.

## Route ID
The number of routes in trips.txt file is larger than the number of routes in stop_times.txt file. This is indicated by the ID's not aligning. This means that some of the routes have not been covered in the stop_time.txt file description.

## Direction
No data was provided for the direction of each of the trips in the trips.txt file.