with open('data/day12input', 'r') as myfile:
    lines = myfile.readlines()

position = (0, 0)
direction = 'east'


def moveForward(amount, eastposition, northposition, direction):
    if direction == 'east':
        eastposition += amount
    elif direction == 'west':
        eastposition -= amount
    elif direction == 'north':
        northposition += amount
    else:
        northposition -= amount
    return tuple((northposition, eastposition))


def turnright(direction):
    if direction == 'east':
        return 'south'
    elif direction == 'south':
        return 'west'
    elif direction == 'west':
        return 'north'
    else:
        return 'east'


def turnleft(direction):
    if direction == 'east':
        return 'north'
    elif direction == 'south':
        return 'east'
    elif direction == 'west':
        return 'south'
    else:
        return 'west'


def turn(dir, amount, direction):
    res = direction
    for i in range(int(amount/90)):
        if dir == 'R':
            res = turnright(res)
        else:
            res = turnleft(res)
    return res


for line in lines:
    letter = line[0]
    digit = int(line[1:])

    if letter == 'F':
        position = moveForward(digit, position[1], position[0], direction)
    elif letter == 'L' or letter == 'R':
        direction = turn(letter, digit, direction)
    elif letter == 'N' or letter == 'S' or letter == 'E' or letter == 'W':
        if letter == 'N':
            position = moveForward(digit, position[1], position[0], 'north')
        elif letter == 'S':
            position = moveForward(digit, position[1], position[0], 'south')
        elif letter == 'W':
            position = moveForward(digit, position[1], position[0], 'west')
        elif letter == 'E':
            position = moveForward(digit, position[1], position[0], 'east')

print(abs(position[0]) + abs(position[1]))

waypoint = (1, 10)
position = (0, 0)


def move(pos, wppos, amount):
    res = list(pos)
    res[0] = pos[0] + amount * wppos[0]
    res[1] = pos[1] + amount * wppos[1]
    return tuple(res)


def singleturnwp(letter, wppos):
    res = list(wppos)
    if letter == 'R':
        temp = res[1] * -1
        res[1] = res[0]
        res[0] = temp
        # if (wppos[0] > 0 and wppos[1] > 0) or (wppos[0] < 0 and wppos[1] < 0):
        #     temp = res[1] * -1
        #     res[1] = res[0]
        #     res[0] = temp
        # elif (wppos[0] < 0 and wppos[1] > 0) or (wppos[0] > 0 and wppos[1] < 0):
        #     temp = res[0] * -1
        #     res[0] = res[1]
        #     res[1] = temp
    elif letter == 'L':
        temp = res[0] * -1
        res[0] = res[1]
        res[1] = temp
        # if (wppos[0] > 0 and wppos[1] > 0) or (wppos[0] < 0 and wppos[1] < 0):
        #     temp = res[0] * -1
        #     res[0] = res[1]
        #     res[1] = temp
        # elif (wppos[0] < 0 and wppos[1] > 0) or (wppos[0] > 0 and wppos[1] < 0):
        #     temp = res[1] * -1
        #     res[1] = res[0]
        #     res[0] = temp
    return tuple(res)


def turnwp(letter, amount, wppos):
    res = tuple(wppos)
    for i in range(int(amount/90)):
        res = singleturnwp(letter, res)
    return res


for line in lines:
    letter = line[0]
    digit = int(line[1:])

    if letter == 'F':
        position = move(position, waypoint, digit)
    elif letter == 'L' or letter == 'R':
        waypoint = turnwp(letter, digit, waypoint)
    elif letter == 'N' or letter == 'S' or letter == 'E' or letter == 'W':
        if letter == 'N':
            waypoint = moveForward(digit, waypoint[1], waypoint[0], 'north')
        elif letter == 'S':
            waypoint = moveForward(digit, waypoint[1], waypoint[0], 'south')
        elif letter == 'W':
            waypoint = moveForward(digit, waypoint[1], waypoint[0], 'west')
        elif letter == 'E':
            waypoint = moveForward(digit, waypoint[1], waypoint[0], 'east')

print(abs(position[0]) + abs(position[1]))