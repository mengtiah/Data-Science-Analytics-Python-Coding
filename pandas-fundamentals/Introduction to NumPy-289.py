## 4. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi=numpy.array(converted_taxi_list)

## 6. Selecting and Slicing Rows and Items from ndarrays ##

row_0=taxi[0]
rows_391_to_500=taxi[391:501]
row_21_column_5=taxi[21,5]

## 7. Selecting Columns and Custom Slicing ndarrays ##

columns_1_4_7=taxi[:,[1,4,7]]
row_99_columns_5_to_8=taxi[99,5:9]
rows_100_to_200_column_14=taxi[100:201,14]

## 9. Vector Math Continued ##

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
trip_mph=trip_distance_miles/trip_length_hours

## 10. Calculating Statistics For 1D ndarrays ##

mph_min = trip_mph.min()
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

## 12. Calculating Statistics For 2D ndarrays ##

taxi_column_means=taxi.mean(axis=0)