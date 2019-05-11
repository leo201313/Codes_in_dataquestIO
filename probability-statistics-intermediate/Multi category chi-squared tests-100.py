## 2. Calculating expected values ##

under_50=.759
up_50=1-under_50
female=.33
male=1-female
pop=32561

males_over50k=up_50*male*pop
males_under50k=under_50*male*pop
females_over50k=up_50*female*pop
females_under50k=under_50*female*pop

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5257.6, 2589.6, 16558.2, 8155.6]
values=[]

for i,ob in enumerate(observed):
    exp=expected[i]
    value=(ob-exp)**2/exp
    values.append(value)
    
chisq_gender_income=sum(values)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5257.6, 2589.6, 16558.2, 8155.6])

chisq_value,pvalue_gender_income=chisquare(observed,expected)

## 5. Cross tables ##

import pandas as pd
table=pd.crosstab(income['sex'],[income['race']])
print(table)

## 6. Finding expected values ##

import numpy as np
from scipy.stats import chi2_contingency
cross_tab=pd.crosstab(income['sex'],[income['race']])

chisq_value,pvalue_gender_race,dof,expected=chi2_contingency(cross_tab)