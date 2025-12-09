from aocd import *
from time import perf_counter

data_input = get_data(day=2, year=2025)

t1_start = perf_counter()
ex1_res = 0
t1_stop = perf_counter()
print('Part A - Answer: ' + str(ex1_res) + ', calculated in ' + str((t1_stop - t1_start) * 1000) + ' ms')

t2_start = perf_counter()
ex2_res = 0
t2_stop = perf_counter()
print('Part B - Answer: ' + str(ex2_res) + ', calculated in ' + str((t2_stop - t2_start) * 1000) + ' ms')
