## 1. Introduction ##

import pandas as pd
import numpy as np
houses=pd.read_csv('AmesHousing_1.txt',sep='\t')
scale_land='ordinal'
scale_roof='nominal'
kitchen_variable='discrete'

## 2. The Mode for Ordinal Variables ##

def get_mod(arr):
    dic={}
    for ele in arr:
        if ele not in dic:
            dic[ele]=0
        else:
            dic[ele]+=1
    return max(dic,key=dic.get)

mode_function=get_mod(houses['Land Slope'])
mode_method=houses['Land Slope'].mode()
same=mode_function==mode_method
    

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return max(counts, key = counts.get),counts

(mode,value_counts)=mode(houses['Roof Style'])






## 4. The Mode for Discrete Variables ##

bedroom_variable='discrete'
bedroom_mode=houses['Bedroom AbvGr'].mode()
price_variable='continuous'
price_mode=houses['SalePrice'].mode()

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)
max_interval=gr_freq_table.sort_values(ascending=False).index[0]
mode=150000
mean=houses['SalePrice'].mean()
median=houses['SalePrice'].median()
sentence_1=True
sentence_2=True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

shape_1='right skew'
shape_2='right skew'
shape_3='left skew'


## 7. Symmetrical Distributions ##

houses['Mo Sold'].plot.kde(xlim=(1,12))
Mode=houses['Mo Sold'].mode().iloc[0]
Median=houses['Mo Sold'].median()
Mean=houses['Mo Sold'].mean()
plt.axvline(x=Mode,color='Green',label='Mode')
plt.axvline(x=Median,color='Orange',label='Median')
plt.axvline(x=Mean,color='Black',label='Mean')
plt.legend()
plt.show()
