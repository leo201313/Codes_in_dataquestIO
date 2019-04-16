## 1. Recap ##

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
first_twelve = unrate[:12]
plt.plot(first_twelve["DATE"],first_twelve["VALUE"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()


## 3. Matplotlib Classes ##

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

## 5. Adding Data ##

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate.loc[:11,"DATE"],unrate.loc[:11,"VALUE"])
ax2.plot(unrate.loc[12:23,"DATE"],unrate.loc[12:23,"VALUE"])
plt.show()

## 6. Formatting And Spacing ##

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

## 7. Comparing Across More Years ##

fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)

row_1 = unrate[:12]
row_2 = unrate[12:24]
row_3 = unrate[24:36]
row_4 = unrate[36:48]
row_5 = unrate[48:60]

ax1.plot(row_1["DATE"],row_1["VALUE"])
ax2.plot(row_2["DATE"],row_2["VALUE"])
ax3.plot(row_3["DATE"],row_3["VALUE"])
ax4.plot(row_4["DATE"],row_4["VALUE"])
ax5.plot(row_5["DATE"],row_5["VALUE"])

plt.show()

## 8. Overlaying Line Charts ##

unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))
plt.plot(unrate[:12]["MONTH"],unrate[:12]["VALUE"],c="red")
plt.plot(unrate[12:24]["MONTH"],unrate[12:24]["VALUE"],c="blue")
plt.show()

## 9. Adding More Lines ##

unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(10,6))
plt.plot(unrate[:12]["MONTH"],unrate[:12]["VALUE"],c="red")
plt.plot(unrate[12:24]["MONTH"],unrate[12:24]["VALUE"],c="blue")
plt.plot(unrate[24:36]["MONTH"],unrate[24:36]["VALUE"],c="green")
plt.plot(unrate[36:48]["MONTH"],unrate[36:48]["VALUE"],c="orange")
plt.plot(unrate[48:60]["MONTH"],unrate[48:60]["VALUE"],c="black")
plt.show()

## 10. Adding A Legend ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    year = str(i+1948)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i],label=year)
plt.legend(loc="upper left")
plt.show()

## 11. Final Tweaks ##

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()