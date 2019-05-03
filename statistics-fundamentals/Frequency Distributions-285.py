## 1. Simplifying Data ##

import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

wnba=pd.read_csv('wnba.csv')
print(wnba.shape)
print(wnba)

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
freq_distro_pos=wnba['Pos'].value_counts()
freq_distro_height=wnba['Height'].value_counts()


## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
age_ascending=wnba['Age'].value_counts().sort_index(ascending=True)
age_descending=wnba['Age'].value_counts().sort_index(ascending=False)


## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)
pts_ordinal_desc=wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]
# Type your answer below

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')
values=wnba['Age'].value_counts().sort_index()
proportion_25=values[25]/len(wnba)
percentage_30=values[30]/len(wnba)*100
percentage_over_30=values.iloc[9:].sum()/len(wnba)*100
percentage_below_23=values.iloc[:3].sum()/len(wnba)*100


## 6. Percentiles and Percentile Ranks ##

wnba = pd.read_csv('wnba.csv')
from scipy.stats import percentileofscore
percentile_rank_half_less=percentileofscore(wnba['Games Played'],17,kind='weak')
percentage_half_more=100-percentile_rank_half_less

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')
describe=wnba['Age'].describe(percentiles=[.25,.5,.75,.95]).iloc[3:]
age_upper_quartile=describe.iloc[3]
age_middle_quartile=describe.iloc[2]
age_95th_percentile=describe.iloc[4]
question1=True
question2=False
question3=True


## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
grouped_freq_table=wnba['PTS'].value_counts(bins=10).sort_index(ascending=False)
grouped_freq_table=grouped_freq_table/len(wnba)*100


## 9. Information Loss ##

import pandas as pd
group1=wnba['MIN'].value_counts(bins=5).sort_index()
group2=wnba['MIN'].value_counts(bins=10).sort_index()
group3=wnba['MIN'].value_counts(bins=15).sort_index()
group4=wnba['MIN'].value_counts(bins=40).sort_index()

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')
intervals=pd.interval_range(start=0,end=600,freq=60)
gr_freq_table_10=pd.Series([0,0,0,0,0,0,0,0,0,0],index=intervals)
for PTS in wnba['PTS']:
    for interval in intervals:
        if PTS in interval:
            gr_freq_table_10.loc[interval]+=1
            
            
