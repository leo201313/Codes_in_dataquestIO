## 1. Individual Values ##

import pandas as pd
import matplotlib.pyplot as plt
houses = pd.read_table('AmesHousing_1.txt')
houses['SalePrice'].plot.kde(xlim=(houses['SalePrice'].min(),houses['SalePrice'].max()))
plt.axvline(houses['SalePrice'].mean(),color='Black',label='Mean')
plt.axvline(houses['SalePrice'].mean()+houses['SalePrice'].std(ddof=0),color='Red',label='Standard deviation')
plt.axvline(220000,color='Orange',label='220000')
plt.legend()
very_expensive=False

## 2. Number of Standard Deviations ##

distance=220000-houses['SalePrice'].mean()
st_devs_away=distance/(houses['SalePrice'].std(ddof=0))


## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()
from numpy import std
def to_z(val,arr,pop=True):
    mean=sum(arr)/len(arr)
    if pop:
        s=std(arr,ddof=0)
    else:
        s=std(arr,ddof=1)
    distance=val-mean
    return distance/s
min_z=to_z(min_val,houses['SalePrice'])
mean_z=to_z(mean_val,houses['SalePrice'])
max_z=to_z(max_val,houses['SalePrice'])

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

neighborhood=['NAmes','CollgCr','OldTown','Edwards','Somerst']
dic_nei={}
for nei in neighborhood:
    dic_nei[nei]=houses[houses['Neighborhood']==nei]['SalePrice']
    
z_nei={k: z_score(200000,arr,bessel=1) for k,arr in dic_nei.items()}
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
stdev_area=houses['Lot Area'].std()
houses['z_area']=houses['Lot Area'].apply(lambda x: ((x-mean_area)/stdev_area))
z_mean_area=houses['z_area'].mean()
z_stdev_area=round(houses['z_area'].std(ddof=0))


## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]
mean_pop=mean(population)
stdev_pop=std(population,ddof=0)
standardized_pop=[]
for ele in population:
    standardized_pop.append((ele-mean_pop)/stdev_pop)
    
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

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof = 0)
houses['z_1'] = houses['index_1'].apply(lambda x: 
                                      (x - mean_index1) / stdev_index1
                                     )

mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof = 0)
houses['z_2'] = houses['index_2'].apply(lambda x: 
                                      (x - mean_index2) / stdev_index2
                                     )

print(houses[['z_1', 'z_2']].head(2))
better='first'

## 9. Converting Back from Z-scores ##

houses['new_z']=houses['z_merged'].apply(lambda x: (x*10+50))
mean_transformed=houses['new_z'].mean()
stdev_transformed=houses['new_z'].std(ddof=0)