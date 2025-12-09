from aocd import *
from time import perf_counter
import math

data_input = get_data(day=2, year=2025)
# data_input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\n1698522-1698528,446443-446449,38593856-38593862,565653-565659,\n824824821-824824827,2121212118-2121212124'


def is_invalid(numb, part):
    numb_str = str(numb)
    for rep_length in range(1, math.floor(len(numb_str) / 2) + 1):
        if part == 'A':
            if numb_str == numb_str[0:rep_length] * 2:
                # print(numb_str + ' is invalid')
                return True
        elif part == 'B':
            if numb_str == numb_str[0:rep_length] * int(len(numb_str) / rep_length):
                # print(numb_str + ' is invalid')
                return True
    return False


t1_start = perf_counter()
ex1_res = 0
for rng in data_input.split(','):
    for i in range(int(rng.split('-')[0]), int(rng.split('-')[1]) + 1):
        ex1_res += i if is_invalid(i, 'A') else 0
t1_stop = perf_counter()
print('Part A - Answer: ' + str(ex1_res) + ', calculated in ' + str((t1_stop - t1_start) * 1000) + ' ms')
submit(ex1_res, part='a', day=2, year=2025)

t2_start = perf_counter()
ex2_res = 0
for rng in data_input.split(','):
    for i in range(int(rng.split('-')[0]), int(rng.split('-')[1]) + 1):
        ex2_res += i if is_invalid(i, 'B') else 0
t2_stop = perf_counter()
print('Part B - Answer: ' + str(ex2_res) + ', calculated in ' + str((t2_stop - t2_start) * 1000) + ' ms')
submit(ex2_res, part='b', day=2, year=2025)
