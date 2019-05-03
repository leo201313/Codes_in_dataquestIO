## 1. Comparing Frequency Distributions ##

rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']
groupp={'rookies':rookies,'little_xp':little_xp,'experienced':experienced,'very_xp':very_xp,'veterans':veterans}
distro={}
for name,data in groupp.items():
    distro[name+'_distro'] = data['Pos'].value_counts()
print(distro)
    
    

## 2. Grouped Bar Plots ##

import seaborn as sns
sns.countplot(x='Exp_ordinal',hue='Pos',data=wnba,order=['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],hue_order=['C', 'F', 'F/C', 'G', 'G/F'])

## 3. Challenge: Do Older Players Play Less? ##

sns.countplot(x='age_mean_relative',hue='min_mean_relative',data=wnba)
result='rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt
wnba[wnba.Age>=27]['MIN'].plot.hist(label='Old',legend=True,histtype='step',ylim=(0,15))
wnba[wnba.Age<27]['MIN'].plot.hist(label='Young',legend=True,histtype='step')

plt.axvline(x=497,label='Average')
plt.legend()
plt.show()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(x=497,label='Average')
plt.legend()
plt.show()

## 7. Strip Plots ##

sns.stripplot(x='Pos',y='Weight',jitter=True,data=wnba)

## 8. Box plots ##

sns.boxplot(x='Pos',y='Weight',data=wnba)

## 9. Outliers ##

iqr=7
lower_bound=11.5
upper_bound=39.5
outliers_low=(wnba['Games Played'] < 11.5).sum()
outliers_high=(wnba['Games Played'] > 39.5).sum()
sns.boxplot(y='Games Played',data=wnba)

