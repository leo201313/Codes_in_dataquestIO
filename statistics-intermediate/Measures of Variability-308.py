## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def to_range(arr):
    return max(arr)-min(arr)

range_by_year={}
for year in range(2006,2011):
    range_by_year[year]=to_range(houses[houses['Yr Sold']==year]['SalePrice'])
    
one=False
two=True



## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]
def to_avd(arr):
    mean=sum(arr)/len(arr)
    ls=[]
    for i in range(len(arr)):
        ls.append(mean-arr[i])
    return sum(ls)/len(ls)

avg_distance=to_avd(C)
print(avg_distance)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]
def to_avd(arr):
    mean=sum(arr)/len(arr)
    ls=[]
    for i in range(len(arr)):
        ls.append(abs(mean-arr[i]))
    return sum(ls)/len(ls)

mad=to_avd(C)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]
def to_variance(arr):
    mean=sum(arr)/len(arr)
    square=[]
    for ele in arr:
        square.append((mean-ele)**2)
    return sum(square)/len(square)

variance_C=to_variance(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]
def to_std(arr):
    mean=sum(arr)/len(arr)
    square=[]
    for ele in arr:
        square.append((mean-ele)**2)
    variance=sum(square)/len(square)
    return variance**(1/2)
standard_deviation_C=to_std(C)


## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

year_var={}
for year in range(2006,2011):
    year_var[year]=standard_deviation(houses[houses['Yr Sold']==year]['SalePrice'])
    
greatest_variability=max(year_var,key=year_var.get)
lowest_variability=min(year_var,key=year_var.get)


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
st_dev1=standard_deviation(sample1)
st_dev2=standard_deviation(sample2)
bigger_spread='sample 2'


## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)
std=[]
import matplotlib.pyplot as plt
for i in range(5000):
    sample=houses['SalePrice'].sample(10,random_state=i)
    std.append(standard_deviation(sample))
    
plt.hist(std)
plt.axvline(standard_deviation(houses['SalePrice']))

## 9. Bessel's Correction ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

pop_stdev = standard_deviation(houses['SalePrice'])
#plt.hist(st_devs)
#plt.axvline(pop_stdev)
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances) - 1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(pop_stdev)

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var
pandas_stdev=sample['SalePrice'].std(ddof=1)
numpy_stdev=std(sample['SalePrice'],ddof=1)
equal_stdevs=pandas_stdev==numpy_stdev
pandas_var=sample['SalePrice'].var(ddof=1)
numpy_var=var(sample['SalePrice'],ddof=1)
equal_vars=numpy_var==pandas_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
var_ls=[]
std_ls=[]
for ele in samples:
    var_ls.append(var(ele,ddof=1))
    std_ls.append(std(ele,ddof=1))
    
equal_stdev=(sum(std_ls)/len(std_ls))==std(population,ddof=0)
equal_var=(sum(var_ls)/len(var_ls))==var(population,ddof=0)