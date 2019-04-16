## 1. Introduction ##

from csv import reader
opened_file = open('potus_visitors_2015.csv')
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

## 4. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911,6,16)
microsoft_founded = dt.datetime(1975,4,4)
man_on_moon = dt.datetime(1969,7,20,20,17)
jfk_shot = dt.datetime(1963,11,22,12,30)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it

date_format = '%m/%d/%y %H:%M'

for row in potus:
    datedata = row[2]
    temp = dt.datetime.strptime(datedata,date_format)
    row[2] = temp
    

## 6. Using Strftime to format dates ##

visitors_per_month ={}
for row in potus:
    stdt = row[2]
    temp = stdt.strftime('%B, %Y',)
    if temp in visitors_per_month:
        visitors_per_month[temp] += 1
    else:
        visitors_per_month[temp] =1
        

## 7. The Time Class ##

appt_times = {}
for row in potus:
    temp_dt = row[2]
    temp_t = temp_dt.time()
    if temp_t in appt_times:
        appt_times[temp_t] += 1
    else:
        appt_times[temp_t] = 1
        
min_time = min(appt_times)
max_time = max(appt_times)

## 10. Summarizing Appointment Lengths ##

for row in potus:
    temp_data = row[3]
    temp_dt = dt.datetime.strptime(temp_data,'%m/%d/%y %H:%M')
    row[3] = temp_dt
    
appt_lengths = []
for row in potus:
    period = row[3] - row[2]
    appt_lengths.append(period)
    
min_length = min(appt_lengths)
max_length = max(appt_lengths)

summ = sum(appt_lengths,dt.timedelta(0))
avg_length = summ / len(appt_lengths)

print(min_length)