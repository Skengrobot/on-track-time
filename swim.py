#!/usr/bin/env python
import re
from pprint import pprint

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
pprint(data)
