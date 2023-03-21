import csv
from csv import DictReader
import numpy
import numpy as np
from DataLogger import DataLogger, Report
import plotly.express as px

time_list = []
day_list = []
afternoon_list = []
day_list_minutes = []
afternoon_list_minutes = []
off_list = []
on_list = []
total_time_list = []
day_list_states = []
hhmm_list = []
# Enter .csv file

filename = input("Enter File Path and Name: ")


# opening the file using "with"
# statement

with open(filename, 'r') as data:
    dict_reader = DictReader(data)
    list_of_dict = list(dict_reader)

dat = DataLogger()
dat.convert_csv(list_of_dict, time_list)
print(time_list)

DataLogger.convert_time_to_int(time_list)
print(time_list)

DataLogger.split_mornings_afternoons(time_list, day_list, afternoon_list)
print("Day List ", day_list)
print("Afternoon List", afternoon_list)

DataLogger.convert_to_minutes(day_list_minutes, day_list)
print(day_list_minutes)

DataLogger.convert_to_minutes(afternoon_list_minutes, afternoon_list)
print(afternoon_list_minutes)

DataLogger.seperate_by_states(day_list, off_list, on_list)
print(off_list)
print(on_list)

total_time_diff = DataLogger.find_difference(on_list, off_list)
print(total_time_diff)

DataLogger.convert_to_minutes(total_time_list, day_list)
print(total_time_list)

total_run_time = DataLogger.find_total_run_time(total_time_list)
print(total_run_time)
shift_id = input("Enter Shift ID: ")
down_time = DataLogger.calculate_downtime(shift_id, total_run_time, total_time_diff)
print(down_time)

DataLogger.list_of_states(day_list, day_list_states)
print(day_list_states)

DataLogger.convert_time_minutes_to_hhmm(day_list_minutes,hhmm_list)
print(hhmm_list)


foo = Report()
foo.initialize_report(time_list, day_list, afternoon_list, day_list_minutes, afternoon_list_minutes, on_list, off_list, total_time_list, day_list_states, hhmm_list, down_time)

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
