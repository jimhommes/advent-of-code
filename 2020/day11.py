import copy

with open('data/day11input', 'r') as myfile:
    lines = myfile.readlines()

for i in range(len(lines)):
    lines[i] = list(lines[i].strip())

preSeats = list()
afterSeats = list(lines)


def getAdjacentSeats(seats, row, col):
    res = []
    maxcol = len(seats[0])
    maxrow = len(seats)
    for i in range(-1, +2):
        for j in range(-1, +2):
            direction = (i, j)
            i_fly = i
            j_fly = j
            while 0 <= (row + i_fly) < maxrow and 0 <= (col + j_fly) < maxcol and not (i_fly == j_fly == 0):
                if seats[row + i_fly][col + j_fly] != '.':
                    res.append(seats[row + i_fly][col + j_fly])
                    break
                else:
                    i_fly += direction[0]
                    j_fly += direction[1]
    return res


def determineSeat(seats, row, col):
    seat = seats[row][col]
    adjacentseats = getAdjacentSeats(seats, row, col)
    if seat == 'L':
        if '#' not in adjacentseats:
            return '#'
        else:
            return 'L'
    elif seat == '#':
        if adjacentseats.count('#') >= 5:
            return 'L'
        else:
            return '#'
    else:
        return '.'


count = 0
while preSeats != afterSeats:
    count += 1
    print("Start Round " + str(count))
    preSeats = copy.deepcopy(afterSeats)
    # for line in preSeats:
    #     print(line)
    print("Changes...")
    for i in range(len(afterSeats)):
        for j in range(len(afterSeats[0])):
            afterSeats[i][j] = determineSeat(preSeats, i, j)
    # for line in afterSeats:
    #     print(line)
    print("End Round " + str(count))

count = 0
for line in preSeats:
    count += line.count('#')
print(count)