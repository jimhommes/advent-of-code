from aocd import *

data_input = get_data(day=1, year=2025)
# data_input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
dial = 50


def dial_right(to_right):
    new_dial = dial + int(to_right)
    while new_dial > 99:
        new_dial = new_dial - 100
    return new_dial


def dial_left(to_left):
    new_dial = dial - int(to_left)
    while new_dial < 0:
        new_dial = new_dial + 100
    return new_dial


ex1_res = 0
for line in data_input.split('\n'):
    print(line)
    if line[0] == 'L':
        dial = dial_left(line[1:])
    elif line[0] == 'R':
        dial = dial_right(line[1:])

    if dial == 0:
        ex1_res += 1
    print('Dial now at ' + str(dial))
    print('Count now at ' + str(ex1_res))

print(ex1_res)
# submit(ex1_res, part='a', day=1, year=2025)

print('-- start part 2')
ex2_res = 0
dial = 50
for line in data_input.split('\n'):
    print(line)
    direction = line[0]
    amount_of_steps = int(line[1:])
    for i in range(amount_of_steps):
        if direction == 'R':
            dial += 1
            if dial > 99:
                dial = 0
        elif direction == 'L':
            dial -= 1
            if dial < 0:
                dial = 99
        if dial == 0:
            ex2_res += 1

print(ex2_res)
submit(ex2_res, part='b', day=1, year=2025)
