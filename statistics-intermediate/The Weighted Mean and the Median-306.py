## 1. Introduction ##

mean_new=houses_per_year['Mean Price'].mean()
mean_original=houses['SalePrice'].mean()
difference=mean_original-mean_new

## 2. Different Weights ##

houses_per_year['sum']=houses_per_year['Mean Price'] * houses_per_year['Houses Sold']
weighted_mean=houses_per_year['sum'].sum()/houses_per_year['Houses Sold'].sum()
mean_original=houses['SalePrice'].mean()
difference=round(mean_original,10)-round(weighted_mean,10)


## 3. The Weighted Mean ##

import numpy as np
def weighted_mean(arr1,arr2):
    mul_ls=[]
    for ele in range(len(arr1)):
        mul = arr1[ele] * arr2[ele]
        mul_ls.append(mul)
    return sum(mul_ls)/sum(arr2)

weighted_mean_function=weighted_mean(houses_per_year['Mean Price'],houses_per_year['Houses Sold'])
weighted_mean_numpy=np.average(houses_per_year['Mean Price'],weights=houses_per_year['Houses Sold'])
equal=weighted_mean_function==weighted_mean_numpy

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1=23
median2=55
median3=32


## 5. Distributions with Even Number of Values ##

houses_temp=houses.copy()
houses_temp['TotRms AbvGrd'].replace(to_replace='10 or more',value=10,inplace=True)
sort_houses=houses_temp['TotRms AbvGrd'].astype(int,copy=True).sort_values(ascending=True)
lent=sort_houses.shape
median=(sort_houses.iloc[1464]+sort_houses.iloc[1465])/2

## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt
houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()
lotarea_difference=houses['Lot Area'].mean()-houses['Lot Area'].median()
saleprice_difference=houses['SalePrice'].mean()-houses['SalePrice'].median()

## 7. The Median for Ordinal Scales ##

mean=houses['Overall Cond'].mean()
median=houses['Overall Cond'].median()
houses['Overall Cond'].plot.hist()
plt.show()
more_representative='mean'