#!/usr/bin/python
import re
from pprint import pprint
import math

def swim_parse():
    dataset = file('./test')

    data = {}
    current_event = {}
    ages = []

    for count,line in enumerate(dataset):
        line = line.replace("\n","")
        if re.findall("[a-zA-Z]", line):
            event = line
            data[event] = {}
            data[event]["male"] = {}
            data[event]["female"] = {}
        
        elif event == "GOLD" and line:
            ages.append(line)
        
        elif line:
            age_index = count % 12 -1
            gender = "female"
            if age_index < 5:
                gender = "male"
            data[event][gender][ages[count % 12 - 1]] = line

    data.pop("GOLD")

    pprint(ages)
    # pprint(data)

    return data

def time_percent(time_string, percent):
    time_array = time_string.split(':')

    if len(time_array) is 2:
        time = 60 * int(time_array[0]) + float(time_array[1])
        time = time + time * 0.01 * percent
        
        minutes = str(int(math.floor(time/60)))
        seconds = str(round(time%60,2))
        if time%60 < 10:
            seconds = '0' + seconds

        output = minutes + ":" + seconds

    if len(time_array) is 1:
        time = float(time_string)
        time += time*0.01*percent

        output = str(round(time,2))

    return output
