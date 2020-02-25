## 1. Introduction ##

mean_new=houses_per_year['Mean Price'].mean()
mean_original=houses['SalePrice'].mean()
difference=mean_original-mean_new

## 2. Different Weights ##

houses_per_year['total']=houses_per_year['Mean Price']*houses_per_year['Houses Sold']
weighted_mean=sum(houses_per_year['total'])/sum(houses_per_year['Houses Sold'])
mean_original=houses['SalePrice'].mean()
difference=round(mean_original,1)-round(weighted_mean,1)

## 3. The Weighted Mean ##

def weight_cal(mean,weight):
    a=sum(mean*weight)
    b=sum(weight)
    weighted_mean=a/b
    return weighted_mean

weighted_mean_function=weight_cal(houses_per_year['Mean Price'],houses_per_year['Houses Sold'])
weighted_mean_numpy=numpy.average(houses_per_year['Mean Price'],weights=houses_per_year['Houses Sold'])
equal=weighted_mean_function==weighted_mean_numpy

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1=23
median2=55
median3=32

## 5. Distributions with Even Number of Values ##

new=houses['TotRms AbvGrd'].replace({'10 or more':10})
new=new.astype(int)
new=new.sort_values(ascending=True)
length=len(new)
m=new.iloc[[length/2,length/2+1]]
median=m.mean()




## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt

houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()
houses['Lot Area'].mean()
houses['Lot Area'].median()
houses['SalePrice'].mean()
houses['SalePrice'].median()
lotarea_difference=houses['Lot Area'].mean()-houses['Lot Area'].median()
saleprice_difference=houses['SalePrice'].mean()-houses['SalePrice'].median()

## 7. The Median for Ordinal Scales ##


mean=houses['Overall Cond'].mean()
median=houses['Overall Cond'].median()
houses['Overall Cond'].hist()
more_representative='mean'

