
def ydownxright(down, right, lines):
    stringLength = len(lines[0]) - 1
    amountOfTrees = 0
    currentPosition = 0

    y = 0
    while y < len(lines):
        line = lines[y]
        if line[currentPosition] == '#':
            amountOfTrees += 1

        currentPosition += right
        if currentPosition >= stringLength:
            currentPosition -= stringLength
        y += down

    return amountOfTrees


with open('data/day3input', 'r') as myfile:
    lines = myfile.readlines()

multiplyTrees = 1
multiplyTrees *= ydownxright(1, 1, lines)
multiplyTrees *= ydownxright(1, 3, lines)
multiplyTrees *= ydownxright(1, 5, lines)
multiplyTrees *= ydownxright(1, 7, lines)
multiplyTrees *= ydownxright(2, 1, lines)

print(multiplyTrees)