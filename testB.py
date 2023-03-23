import csv
from csv import DictReader
import numpy
import numpy as np
from DataLogger import DataLogger
import plotly.express as px

time_list = []
day_list = []
afternoon_list = []
day_list_minutes = []
afternoon_list_minutes = []
off_list = []
on_list = []
day_total_time_list = []
afternoon_total_time_list = []
day_list_states = []
afternoon_list_states = []
day_hhmm_list = []
afternoon_hhmm_list = []

day_on_list = []
day_off_list = []
afternoon_on_list = []
afternoon_off_list = []

# Enter .csv file

filename = input("Enter File Path and Name: ")


# opening the file using "with"
# statement

with open(filename, 'r') as data:
    dict_reader = DictReader(data)
    list_of_dict = list(dict_reader)

# Create dat instance of DataLogger and convert csv data into list of time and states
dat = DataLogger()
dat.convert_csv(list_of_dict, time_list)
#print(time_list)

# Convert Time to int
DataLogger.convert_time_to_int(time_list)
#print(time_list)

DataLogger.split_mornings_afternoons(time_list, day_list, afternoon_list)
print("Day List ", day_list)
print("Afternoon List", afternoon_list)



# Seperate day list and afternoon lists by states
DataLogger.seperate_by_states(day_list, day_off_list, day_on_list)
DataLogger.seperate_by_states(afternoon_list, afternoon_off_list, afternoon_on_list)
print("Afternoon Off Minutes: ", afternoon_off_list)
print("Afternoon On Minutes",afternoon_on_list)

# Convert day list and afternoon list to minutes
DataLogger.convert_to_minutes(day_list_minutes, day_list)
DataLogger.convert_to_minutes(afternoon_list_minutes, afternoon_list)
print("Afternoon Minutes: ",afternoon_list_minutes)

# Find the total time difference to find time state is off
afternoon_total_time_diff = DataLogger.find_difference(afternoon_off_list, afternoon_on_list)
day_total_time_diff = DataLogger.find_difference(day_on_list, day_off_list)

print("Afternoon Time Difference: ",afternoon_total_time_diff)
print("Day Time Difference: ",day_total_time_diff)

# Convert total times to minutes
DataLogger.convert_to_minutes(day_total_time_list, day_list)
DataLogger.convert_to_minutes(afternoon_total_time_list, afternoon_list)
print("Afternoon Total Times: ", afternoon_total_time_list)

# Find total run times for each shift
day_total_run_time = DataLogger.find_total_run_time(day_total_time_list)
afternoon_total_run_time = DataLogger.find_total_run_time(afternoon_total_time_list)
print("Day Total Run Time: ",day_total_run_time)
print("Afternoon Total Run Time: ",afternoon_total_run_time)

# Calculate Downtimes
day_down_time = DataLogger.calculate_downtime('Days', day_total_run_time, day_total_time_diff)
afternoon_down_time = DataLogger.calculate_downtime('Afternoons', afternoon_total_run_time, afternoon_total_time_diff)
print("Day Downtime: ",day_down_time)
print("Afternoon Downtime: ",afternoon_down_time)

DataLogger.list_of_states(day_list, day_list_states)
DataLogger.list_of_states(afternoon_list, afternoon_list_states)
#print(day_list_states)

DataLogger.convert_time_minutes_to_hhmm(day_list_minutes,day_hhmm_list)
DataLogger.convert_time_minutes_to_hhmm(afternoon_list_minutes,afternoon_hhmm_list)
print(day_hhmm_list)
print(afternoon_hhmm_list)
print("Total Downtime: ", '{:02d}:{:02d}'.format(*divmod(day_down_time, 60)))
print("Total Downtime: ", '{:02d}:{:02d}'.format(*divmod(afternoon_down_time, 60)))


#print(foo.display(time_list, day_list, afternoon_list, day_list_minutes, afternoon_list_minutes, on_list, off_list, total_time_list, day_list_states, hhmm_list, down_time))

"""""
foo = Report()
foo.time_list = time_list
foo.day_list = day_list
foo.afternoon_list = afternoon_list
print(foo.time_list)
print(foo.day_list)
print(foo.afternoon_list)



fig = px.line(x=hhmm_list, y=day_list_states, title="March 16 Day Shift")
print(fig)
fig.show()
"""
