import csv
from csv import DictReader
import numpy
import numpy as np

#Enter .csv file

filename = input("Enter File Path and Name: ")


# opening the file using "with"
# statement

with open(filename, 'r') as data:
    dict_reader = DictReader(data)
    list_of_dict = list(dict_reader)

# Create list to store elements from columns
time_list = []
old_time = []
off_list = []
on_list = []
day_list = []
afternoon_list = []
time_list_minutes = []

total = 0
res = 0
total_time_diff = 0

# Find the difference between on and off times
def Find_Difference(list, total_time_diff, res):
    for z in range(len(on_list)-1):
        res = on_list[z] - off_list[z]
        total_time_diff = total_time_diff + res
        #print(total_time_diff)
    return total_time_diff

# Iterate through csv data and find all elements under Time key
# remove dd/mm/yyyy and store time, and input in new_list
for val in list_of_dict:
    k = (val['Time'])
    zet = (k.split(' '))
    p = (val['Ext. Input 1 digital'])
    #print(p)
    time_list.append(zet[1].split(':') + [p])




#print(time_list)
#print(input_list)

# Convert hours and minutes to int Convert hours to minutes

for i in range(len(time_list)-1):
    #print(time_list[i])
    time_list[i][0] = int(time_list[i][0])
    time_list[i][1] = int(time_list[i][1])
    # add all off signal times to off_list and all on signal times to on_list
    if time_list[i][2] == '1oFF' and time_list[i-1][2] != '1off':
        off_list.append(time_list[i][0] * 60 + time_list[i][1])
    elif time_list[i][2] == '1 on' and time_list[i-1][2] != '1 on':
        on_list.append(time_list[i][0] * 60 + time_list[i][1])

print(off_list)
print(on_list)

for q in range(len(time_list)-1):
    time_list_minutes.append(time_list[q][0] * 60 + time_list[q][1])

for t in range(len(time_list_minutes)-1):
    if time_list_minutes[t] < 900:
        day_list.append(time_list_minutes[t])
    if time_list_minutes[t] > 900:
        afternoon_list.append(time_list_minutes[t])

print(time_list_minutes)
print(day_list)
print(afternoon_list)



print(Find_Difference(day_list, total_time_diff, res))

# Find total run time
for s in range(len(off_list)-1):
    #print(comp_list[s])
    old_time = off_list[s]
    new_time = off_list[s+1]

    if new_time < old_time:
        new_time = new_time + 24*60
    res = new_time - old_time
    #print(res)
    total = total + res

#print(total)
#print(total_time_diff)

"""""
# Calculate total off time
if total_time_diff > 0:
    down_time = total - total_time_diff
elif total_time_diff < 0:
    down_time = total + total_time_diff

print("Total Downtime: ", '{:02d}:{:02d}'.format(*divmod(down_time, 60)))
print("Estimated Downtime With Breaks: ", '{:02d}:{:02d}'.format(*divmod(down_time-90, 60)))
"""
