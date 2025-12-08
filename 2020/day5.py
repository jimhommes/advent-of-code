
with open('data/day5input', 'r') as myfile:
    lines = myfile.readlines()

availableSeats = list(range(923))
registered = []

def getSeatID(str):
    rowStr = str[0:7]
    colStr = str[7:10]
    value = 128
    currentRow = 0
    for char in rowStr:
        value = value / 2
        if char == 'B':
            currentRow += value
    value = 8
    currentCol = 0
    for char in colStr:
        value = value / 2
        if char == 'R':
            currentCol += value

    return currentRow * 8 + currentCol

for line in lines:
    val = getSeatID(line)
    availableSeats.remove(val)
    registered.append(val)

for rm in range(8):
    availableSeats.remove(rm)
    
print(availableSeats)