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

# Create list to store elements from column 1
time_list = []
input_list = []
old_time = []
off_list = []
on_list = []
total = 0
res = 0
total_time_diff = 0
# Iterate through csv data and find all elements under Time key
# remove dd/mm/yyyy and store time, and input in new_list
for val in list_of_dict:
    k = (val['Time'])
    zet = (k.split(' '))
    p = (val['Ext. Input 1 digital'])
    #print(p)
    time_list.append(zet[1].split(':') + [p])


    #print(input_list)

#print(time_list)
#print(input_list)

# Convert hours and minutes to int Convert hours to minutes

for i in range(len(time_list)-1):
    #print(time_list[i])
    time_list[i][0] = int(time_list[i][0])
    time_list[i][1] = int(time_list[i][1])
    # add all off signal times to off_list and all on signal times to on_list
    if time_list[i][2] == '1oFF':
        off_list.append(time_list[i][0] * 60 + time_list[i][1])
    elif time_list[i][2] == '1 on':
        on_list.append(time_list[i][0] * 60 + time_list[i][1])

#print(off_list)
#print(on_list)

# Find the difference between on and off times
for z in range(len(on_list)-1):
    res = on_list[z] - off_list[z]
    total_time_diff = total_time_diff + res
#print(total_time_diff)

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

# Calculate total off time
down_time = total + total_time_diff
print("Total Downtime: ", '{:02d}:{:02d}'.format(*divmod(down_time, 60)))