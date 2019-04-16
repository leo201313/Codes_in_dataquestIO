## 2. Introduction to the Data Set ##

import pandas as pd
titanic = pd.read_csv("train.csv")
cols = ["Survived","Pclass","Sex","Age","SibSp","Parch","Fare","Embarked"]
titanic = titanic[cols]
titanic = titanic.dropna()

## 3. Creating Histograms In Seaborn ##

import seaborn as sns 
import matplotlib.pyplot as plt

sns.distplot(titanic["Age"])
plt.show()

## 4. Generating A Kernel Density Plot ##

sns.kdeplot(titanic["Age"],shade = True)
plt.xlabel("Age")

## 5. Modifying The Appearance Of The Plots ##

sns.set_style("white")
sns.kdeplot(titanic["Age"],shade=True)
plt.xlabel("Age")
sns.despine(left=True,bottom=True)

## 6. Conditional Distributions Using A Single Condition ##

grd = sns.FacetGrid(titanic,col="Pclass",size=6)
grd.map(sns.kdeplot,"Age",shade=True)
sns.despine(left=True,bottom=True)
plt.show()

## 7. Creating Conditional Plots Using Two Conditions ##

g = sns.FacetGrid(titanic, col="Pclass", row="Survived")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex",size=3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

grd = sns.FacetGrid(titanic,col="Survived",row="Pclass",hue="Sex",size=3)
grd.map(sns.kdeplot,"Age",shade=True)
grd.add_legend()
sns.despine(left=True,bottom=True)
plt.show()