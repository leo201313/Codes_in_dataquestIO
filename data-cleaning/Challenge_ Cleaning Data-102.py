## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
head_av=avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
plt.show()
true_avengers = avengers[avengers['Year']>=1960]

## 5. Consolidating Deaths ##

death_fields = ['Death1','Death2','Death3','Death4','Death5']
def to_change(ele):
    ele = str(ele)
    if ele=='YES':
        return 1
    else:
        return 0
    
temp = true_avengers.loc[:,death_fields].applymap(to_change)
temp['Deaths'] = temp.sum(axis=1)
# print(true_avengers.loc[:,death_fields])
true_avengers['Deaths'] = temp['Deaths']

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()
right_year = true_avengers[true_avengers['Years since joining']==(2015-true_avengers['Year'])]
joined_accuracy_count = right_year.shape[0]
