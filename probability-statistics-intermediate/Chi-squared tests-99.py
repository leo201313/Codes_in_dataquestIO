## 2. Calculating differences ##

female_diff=(10771-16280.5)/16280.5
male_diff=(21790-16280.5)/16280.5


## 3. Updating the formula ##

female_diff=(10771-16280.5)**2/16280.5
male_diff=(21790-16280.5)**2/16280.5
gender_chisq=male_diff+female_diff


## 4. Generating a distribution ##

import numpy as np
import matplotlib.pyplot as plt

chi_squared_values = []
expect_count=16280.5
for i in range(1000):
    rand=np.random.random(32561)
    rand[rand<.5]=0
    rand[rand>=.5]=1
    female_count=len(rand[rand==1])
    male_count=len(rand[rand==0])
    male_diff=(male_count-expect_count)**2/expect_count
    female_diff=(female_count-expect_count)**2/expect_count
    chi_squared_values.append(male_diff+female_diff)
    
plt.hist(chi_squared_values)
plt.show()

## 6. Smaller samples ##

female_diff=(107.71-162.805)**2/162.805
male_diff=(217.90-162.805)**2/162.805
gender_chisq=female_diff+male_diff

## 7. Sampling distribution equality ##

import numpy as np
import matplotlib.pyplot as plt
chi_squared_values = []
for i in range(1000):
    rand=np.random.random(300)
    rand[rand<.5]=0
    rand[rand!=0]=1
    male_count=len(rand[rand==0])
    female_count=len(rand[rand==1])
    male_diff=(male_count-150)**2/150
    female_diff=(female_count-150)**2/150
    chi_squared_values.append(male_diff+female_diff)
    
plt.hist(chi_squared_values)
plt.show()

## 9. Increasing degrees of freedom ##

import numpy as np
diffs = []
observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])
diff=(observed-expected)**2/expected
race_chisq=diff.sum()



## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np
observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

race_chisq,race_pvalue=chisquare(observed,expected)