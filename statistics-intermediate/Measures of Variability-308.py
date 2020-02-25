## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')
def find_range(x):
    return max(x)-min(x)

range_by_year={}
for i in houses['Yr Sold'].unique():
    data_by_year=houses[houses['Yr Sold']==i]
    range_by_year[i]=find_range(data_by_year['SalePrice'])

one=False
two=True
        
    


## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]
def average_distance(x):
    count=0
    diff_list=[]
    average=sum(x)/len(x)
    for i in x:
        count+=1
        diff=i-average
        diff_list.append(diff)
    return sum(diff_list)/count
avg_distance=average_distance(C)
print(avg_distance)
        

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]
def mean_absolute_deviation(x):
    length=len(x)
    average=sum(x)/length
    diff=[]
    for i in x:
        dis=abs(i-average)
        diff.append(dis)
    return sum(diff)/length
mad=mean_absolute_deviation(C)
              
    

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]
def squared_distance(x):
    length=len(x)
    average=sum(x)/length
    diff=[]
    for i in x:
        dis=(i-average)**2
        diff.append(dis)
    return sum(diff)/length
variance_C=squared_distance(C)
              
    

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]
def standard_deviation(x):
    length=len(x)
    average=sum(x)/length
    diff=[]
    for i in x:
        dis=(i-average)**2
        diff.append(dis)
    return sqrt(sum(diff)/length)
standard_deviation_C=standard_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)
years={}
for i in houses['Yr Sold'].unique():
    year_segment=houses[houses['Yr Sold']==i]
    st_dev=standard_deviation(year_segment['SalePrice'])
    years[i]=st_dev
greatest_variability=max(years,key=years.get)
lowest_variability=min(years,key=years.get)

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread='sample 2'
st_dev1=standard_deviation(sample1)
st_dev2=standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
total=[]
for i in range(5000):
    total.append(standard_deviation(houses['SalePrice'].sample(10,random_state=i)))
 
plt.hist(total)
plt.axvline(standard_deviation(houses['SalePrice']))

## 9. Bessel's Correction ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
#plt.hist(st_devs)
#plt.axvline(standard_deviation(houses['SalePrice']))
plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var
pandas_stdev=sample['SalePrice'].std(ddof=1)
numpy_stdev=std(sample['SalePrice'],ddof=1)

equal_stdevs=pandas_stdev==numpy_stdev
pandas_var=sample['SalePrice'].var(ddof = 1)
numpy_var=var(sample['SalePrice'], ddof = 1)
equal_vars=pandas_var==numpy_var


## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
equal_var=var(population)==var(sample).mean()

equal_stdev=std(population)==std(sample).mean()
