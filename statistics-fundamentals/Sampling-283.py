## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
print(wnba.head())
print(wnba.tail())
shapee=wnba.shape
parameter=wnba['Games Played'].max()
sample=wnba['Games Played'].sample(random_state=1)
statistic=sample.max()
sampling_error=parameter-statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
sample_means=[]
population_mean=wnba['PTS'].mean()

for i in range(100):
    sample=wnba['PTS'].sample(10,random_state=i)
    sample_means.append(sample.mean())
    
plt.scatter(range(1,101),sample_means)
plt.axhline(population_mean)

## 7. Stratified Sampling ##

wnba['score_per_game']=wnba['PTS'] / wnba['Games Played']
stratum_G = wnba[wnba.Pos == 'G']
stratum_F = wnba[wnba.Pos == 'F']
stratum_C = wnba[wnba.Pos == 'C']
stratum_GF = wnba[wnba.Pos == 'G/F']
stratum_FC = wnba[wnba.Pos == 'F/C']

Pos={}
for val,name in [(stratum_G,'G'),(stratum_F,'F'),(stratum_C,'C'),(stratum_GF,'GF'),(stratum_FC,'FC')]:
    Pos[name]=val['score_per_game'].sample(10,random_state=0).mean()

position_most_points=''
most_points_position=0
for name,val in Pos.items():
    if val >= most_points_position:
        position_most_points=name
        most_points_position=val


## 8. Proportional Stratified Sampling ##

group_low=wnba[wnba['Games Played']<=12]
group_mid=wnba[(wnba['Games Played']>12) & (wnba['Games Played']<=22)]
group_high=wnba[wnba['Games Played']>22]

mean_pts=[]

for ele in range(100):
    low_sample=group_low.sample(1,random_state=ele)
    mid_sample=group_mid.sample(2,random_state=ele)
    high_sample=group_high.sample(7,random_state=ele)
    mix_sample=pd.concat([low_sample,mid_sample,high_sample])
    mean_pts.append(mix_sample['PTS'].mean())
    
plt.scatter(range(1,101),mean_pts)
plt.axhline(wnba['PTS'].mean())

## 9. Choosing the Right Strata ##

wnba['MIN'].value_counts(bins = 3, normalize = True)
low_sample=wnba[wnba['MIN']<=347.333]
mid_sample=wnba[(wnba['MIN']<=682.667)&(wnba['MIN']>347.333)]
high_sample=wnba[wnba['MIN']>682.667]

mean_group=[]

for ele in range(100):
    mix_group=pd.concat([low_sample.sample(4,random_state=ele),mid_sample.sample(4,random_state=ele),high_sample.sample(4,random_state=ele)])
    mean_group.append(mix_group['PTS'].mean())
    
plt.scatter(range(1,101),mean_group)
plt.axhline(wnba["PTS"].mean())

## 10. Cluster Sampling ##

teams=pd.Series(wnba['Team'].unique()).sample(4, random_state = 0).tolist()

def yes_not(ele):
    if ele in teams:
        return True
    else:
        return False

sample=wnba[wnba['Team'].apply(yes_not)]
sampling_error_height=wnba['Height'].mean()-sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()