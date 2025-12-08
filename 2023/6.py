import re
import numpy as np

starting_speed = 0
accel = 1

with open('input/6.txt') as f:
    lines = f.readlines()

times = [int(x) for x in re.findall(r'\d+', lines[0])]
distances = [int(x) for x in re.findall(r'\d+', lines[1])]

res = []
for race_index in range(len(times)):
    time = times[race_index]
    distance = distances[race_index]

    amount_valid = 0
    for button_hold_time in range(1, time):
        total_distance = (time - button_hold_time) * (button_hold_time)
        if total_distance > distance:
            amount_valid += 1
    res.append(amount_valid)

print(np.prod(res))

times = [int(x) for x in re.findall(r'\d+', lines[0].replace(' ', ''))]
distances = [int(x) for x in re.findall(r'\d+', lines[1].replace(' ', ''))]

res = []
for race_index in range(len(times)):
    time = times[race_index]
    distance = distances[race_index]

    amount_valid = 0
    for button_hold_time in range(1, time):
        total_distance = (time - button_hold_time) * (button_hold_time)
        if total_distance > distance:
            amount_valid += 1
    res.append(amount_valid)

print(res[0])
