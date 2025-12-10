from aocd import *
from time import perf_counter

data_input = get_data(day=3, year=2025)
# data_input = '987654321111111\n811111111111119\n234234234234278\n818181911112111'


def get_maximum_joltage(bank, battery_length):
    return int(get_maximum_joltage_rec(bank, battery_length, 1))


def get_maximum_joltage_rec(current_bank, battery_length, current_depth):
    for i in reversed(range(10)):
        if str(i) in current_bank[0:len(current_bank)-(battery_length-current_depth)]:
            if battery_length == current_depth:
                return str(i)
            else:
                rec_res = get_maximum_joltage_rec(current_bank[current_bank.index(str(i))+1:], battery_length, current_depth + 1)
                if rec_res is not None:
                    return str(i) + rec_res
    return None


t1_start = perf_counter()
ex1_res = 0
for line in data_input.split('\n'):
    ex1_res += get_maximum_joltage(line, 2)
t1_stop = perf_counter()
print('Part A - Answer: ' + str(ex1_res) + ', calculated in ' + str((t1_stop - t1_start) * 1000) + ' ms')
# submit(ex1_res, part='a', day=3, year=2025)

t2_start = perf_counter()
ex2_res = 0
for line in data_input.split('\n'):
    ex2_res += get_maximum_joltage(line, 12)
t2_stop = perf_counter()
print('Part B - Answer: ' + str(ex2_res) + ', calculated in ' + str((t2_stop - t2_start) * 1000) + ' ms')
submit(ex2_res, part='b', day=3, year=2025)
