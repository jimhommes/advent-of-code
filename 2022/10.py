class Sprite:
    def __init__(self):
        self.x = 1
        self.y = 1


def get_current_pixel(cyc, x):
    position_crt = (cyc-1) % 40
    res = ''
    if position_crt == 0:
        res += '\n'
    if abs(position_crt - x) > 1:
        res += '.'
    else:
        res += '#'
    return res


with open('input/10.txt') as f:
    lines = f.readlines()

# Part 1
X = 1
cycle = 0
values = []

# Part 2
display = ''

for line in lines:
    spl = line.strip().split(' ')
    if spl[0] == 'noop':
        # Execute noop
        # First Cycle
        cycle += 1
        values.append(X)
        display += get_current_pixel(cycle, X)
        print('Cycle: ' + str(cycle) + ', X: ' + str(X))
    elif spl[0] == 'addx':
        # Execute addx
        # First Cycle
        cycle += 1
        values.append(X)
        display += get_current_pixel(cycle, X)
        print('Cycle: ' + str(cycle) + ', X: ' + str(X))

        # Second Cycle
        cycle += 1
        values.append(X)
        display += get_current_pixel(cycle, X)
        print('Cycle: ' + str(cycle) + ', X: ' + str(X))
        X += int(spl[1])

res_cycles = [20, 60, 100, 140, 180, 220]
res_values = [values[i - 1] * i for i in res_cycles]
print(res_values)
print(sum(res_values))
print(display)