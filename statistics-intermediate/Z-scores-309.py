## 1. Individual Values ##

import pandas as pd
import numpy as np
houses = pd.read_table('AmesHousing_1.txt')
houses['SalePrice'].plot.kde(xlim=(min(houses['SalePrice']),max(houses['SalePrice'])))
plt.axvline(houses['SalePrice'].mean(),label='Mean',color='black')
plt.axvline(houses['SalePrice'].std(ddof = 0)+houses['SalePrice'].mean(),label='Standard deviation',color='red')
plt.axvline(220000,label='220000',color='orange')
plt.legend()
very_expensive=False

## 2. Number of Standard Deviations ##

st_devs_away=(220000-houses['SalePrice'].mean())/houses['SalePrice'].std(ddof=0)

## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def compute(x,array):
    mean_value=array.mean()
    st_dev=array.std(ddof=0)
    distance=x-mean_value
    z_score=distance/st_dev
    return z_score
min_z=compute(min_val,houses['SalePrice'])
mean_z=compute(mean_val,houses['SalePrice'])
max_z=compute(max_val,houses['SalePrice'])
    

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

NAmes=z_score(200000,houses[houses['Neighborhood'] == 'NAmes']['SalePrice'],bessel=0)
CollgCr=z_score(200000,houses[houses['Neighborhood'] == 'CollgCr']['SalePrice'],bessel=0)
OldTown=z_score(200000,houses[houses['Neighborhood'] == 'OldTown']['SalePrice'],bessel=0)
Edwards=z_score(200000,houses[houses['Neighborhood'] == 'Edwards']['SalePrice'],bessel=0)
Somerst=z_score(200000,houses[houses['Neighborhood'] == 'Somerst']['SalePrice'],bessel=0)

best_investment='College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )
z_mean_price=houses['z_prices'].mean()
z_stdev_price=houses['z_prices'].std(ddof=0)
mean_area=houses['Lot Area'].mean()
stdev_area=houses['Lot Area'].std(ddof=0)
houses['z_area']=houses['Lot Area'].apply(lambda x:((x-mean_area)/stdev_area))
z_mean_area=houses['z_area'].mean()
z_stdev_area=houses['z_area'].std(ddof=0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]
standardized_pop=[]
mean_pop = mean(population)
stdev_pop = std(population, ddof = 0)
for i in population:
    z=(i-mean_pop)/stdev_pop
    standardized_pop.append(z)
    
mean_z=mean(standardized_pop)
stdev_z=std(standardized_pop,ddof=0)

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
stdev_sample=std(standardized_sample,ddof=1)

## 8. Using Standardization for Comparisons ##

mean1=houses['index_1'].mean()
std1=houses['index_1'].std()
mean2=houses['index_2'].mean()
std2=houses['index_2'].std()
transindex_1=[]
transindex_2=[]
for i in houses['index_1']:
    z=(i-mean1)/std1
    transindex_1.append(z)
for j in houses['index_2']:
    z=(j-mean2)/std2
    transindex_2.append(z)
print(transindex_1[1])
print(transindex_2[0])
better='first'

## 9. Converting Back from Z-scores ##

x=10*houses['z_merged']+50
mean_transformed=x.mean()
stdev_transformed=x.std(ddof=0)