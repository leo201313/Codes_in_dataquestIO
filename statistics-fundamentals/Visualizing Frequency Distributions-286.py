## 2. Bar Plots ##

# Experience_index=['Rookie','Little experience','Experienced','Very experienced','Veteran']
# Exp_ordinal=pd.Series([0,0,0,0,0],index=Experience_index)
# def distt(ele):
#     ele=int(ele)
#     if ele == 0:
#         Exp_ordinal['Rookie']+=1
#     elif ele <= 3:
#         Exp_ordinal['Little experience']+=1
#     elif ele <= 5:
#         Exp_ordinal['Experienced']+=1
#     elif ele <= 10:
#         Exp_ordinal['Very experienced']+=1
#     else:
#         Exp_ordinal['Veteran']+=1

# wnba['Experience'].apply(distt)
# Exp_ordinal.plot.bar()
wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()

## 3. Horizontal Bar Plots ##

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title='Number of players in WNBA by level of experience')

## 4. Pie Charts ##

wnba['Exp_ordinal'].value_counts().plot.pie()

## 5. Customizing a Pie Chart ##

import matplotlib.pyplot as plt

wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), autopct = '%.2f%%',
                                    title = 'Percentage of players in WNBA by level of experience')
plt.ylabel('')

## 6. Histograms ##

wnba['PTS'].plot.hist()

## 7. The Statistics Behind Histograms ##

percentilis=wnba['Games Played'].describe().iloc[3:]
wnba['Games Played'].plot.hist()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range=(1,32),bins=8,title='The distribution of players by games played')
plt.xlabel('Games played')

## 10. Skewed Distributions ##

wnba['AST'].plot.hist()
plt.show()
wnba['FT%'].plot.hist()
assists_distro='right skewed'
ft_percent_distro='left skewed'

## 11. Symmetrical Distributions ##

wnba['Age'].plot.hist()
plt.show()
wnba['Height'].plot.hist()
plt.show()
wnba['MIN'].plot.hist()
plt.show()
normal_distribution='Height'