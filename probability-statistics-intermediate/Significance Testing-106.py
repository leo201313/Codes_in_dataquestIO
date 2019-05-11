## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a=np.mean(weight_lost_a)
mean_group_b=np.mean(weight_lost_b)
print(mean_group_a)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference=mean_group_b-mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)
mean_differences=[]
for i in range(1000):
    group_a=[]
    group_b=[]
    for ele in all_values:
        if np.random.rand() >= 0.5:
            group_a.append(ele)
        else:
            group_b.append(ele)
    iteration_mean_difference=np.mean(group_b)-np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)    


## 7. Dictionary representation of a distribution ##

sampling_distribution={}
for ele in mean_differences:
    if sampling_distribution.get(ele,False):
        sampling_distribution[ele]+=1
    else:
        sampling_distribution[ele]=1

## 8. P value ##

frequencies=[]
for ele in sampling_distribution:
    if ele >= 2.52:
        frequencies.append(sampling_distribution[ele])
        
p_value=np.sum(frequencies)/1000        