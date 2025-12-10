from aocd import *
from time import perf_counter

data_input = get_data(day=3, year=2025)
# data_input = '987654321111111\n811111111111119\n234234234234278\n818181911112111'


def get_maximum_joltage(bank):
    for i in reversed(range(10)):
        for j in reversed(range(10)):
            if str(i) in bank and str(j) in bank[bank.index(str(i))+1:]:
                return int(str(i) + str(j))


t1_start = perf_counter()
ex1_res = 0
for line in data_input.split('\n'):
    ex1_res += get_maximum_joltage(line)
t1_stop = perf_counter()
print('Part A - Answer: ' + str(ex1_res) + ', calculated in ' + str((t1_stop - t1_start) * 1000) + ' ms')
submit(ex1_res, part='a', day=3, year=2025)

# t2_start = perf_counter()
# ex2_res = 0
# t2_stop = perf_counter()
# print('Part B - Answer: ' + str(ex2_res) + ', calculated in ' + str((t2_stop - t2_start) * 1000) + ' ms')
# submit(ex2_res, part='b', day=3, year=2025)
