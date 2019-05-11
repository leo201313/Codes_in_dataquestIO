## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
mean=sum(distribution)/len(distribution)
center=False
equal_distances=True

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed

equal_distances = -7

for ele in range(5000):
    seed(ele)
    distribution=randint(0,1000,10)
    mean=sum(distribution)/len(distribution)
    above=[]
    below=[]
    for value in distribution:
        if value == mean:
            continue
        elif value > mean:
            above.append(value-mean)
        elif value < mean:
            below.append(mean-value)
        sum_above = round(sum(above),1)
        sum_below = round(sum(below),1)
        if (sum_above==sum_below):
            equal_distances += 1
# from numpy.random import randint, seed
# equal_distances = 0

# for i in range(5000):
#     seed(i)
#     distribution = randint(0,1000,10)
#     mean = sum(distribution) / len(distribution)
    
#     above = []
#     below = []
#     for value in distribution:
#         if value == mean:
#             continue # continue with the next iteration because the distance is 0
#         if value < mean:
#             below.append(mean - value)
#         if value > mean:
#             above.append(value - mean)
    
#     sum_above = round(sum(above),1)
#     sum_below = round(sum(below),1)
#     if (sum_above == sum_below):
#         equal_distances += 1

## 4. Defining the Mean Algebraically ##

one=False
two=False
three=False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def meann(arr):
    summ=0
    for i in range(len(arr)):
        summ+=arr[i]
    return summ/len(arr)
mean_1=meann(distribution_1)
mean_2=meann(distribution_2)
mean_3=meann(distribution_3)

## 6. Introducing the Data ##

import pandas as pd 
import numpy as np
houses = pd.read_csv('AmesHousing_1.txt',sep='\t')
head=houses.head()
one=True
two=False
three=True


## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)
function_mean=mean(houses['SalePrice'])
pandas_mean=houses['SalePrice'].mean()
means_are_equal=pandas_mean==function_mean

## 8. Estimating the Population Mean ##

import matplotlib.pyplot as plt
total_mean=houses['SalePrice'].mean()
sampling_errors=[]
sample_sizes=[]
sample_size=5
for ele in range(101):
    houses_sample=houses['SalePrice'].sample(sample_size,random_state=ele)
    sampling_error=total_mean-houses_sample.mean()
    sampling_errors.append(sampling_error)
    sample_sizes.append(sample_size)
    sample_size+=29
    
plt.scatter(sample_sizes,sampling_errors)
plt.axhline(y=0)
plt.axvline(x=2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')
plt.show()
    

## 9. Estimates from Low-Sized Samples ##

means=[]
for ele in range(10000):
    house_sample=houses['SalePrice'].sample(100,random_state=ele)
    means.append(house_sample.mean())
    
plt.hist(means)
plt.axvline(x=houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]
def meann(arr):
    summ=0
    for i in range(len(arr)):
        summ+=arr[i]
    return summ/len(arr)
population_mean=meann(population)
sub_population=[[3,7],[3,2],[7,2]]
mean_of_sample_means=[]
for ar in sub_population:
    mean_of_sample_means.append(meann(ar))
    
unbiased=meann(mean_of_sample_means)==population_mean    