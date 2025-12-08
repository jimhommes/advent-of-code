
with open('data/day8input', 'r') as myfile:
    lines = myfile.readlines()

jumpToNop = True

for i in range(len(lines)):
    if lines[i].split(" ")[0] == "nop":
        jumpToNop = False
    elif lines[i].split(" ")[0] == "jmp":
        jumpToNop = True

    if lines[i].split(" ")[0] == "nop" or lines[i].split(" ")[0] == "jmp":
        currentIndex = 0
        visitedIndices = []
        accumulator = 0
        while currentIndex < len(lines):
            spl = lines[currentIndex].split(" ")
            if currentIndex in visitedIndices:
                print("Index " + str(currentIndex) + " al in lijst.")
                print("Loop afgebroken, accumulator: " + str(accumulator))
                break
            else:
                visitedIndices.append(currentIndex)

            if currentIndex == i:
                if jumpToNop:
                    spl[0] = 'nop'
                else:
                    spl[0] = 'jmp'

            if spl[0] == 'nop':
                currentIndex += 1
            elif spl[0] == 'acc':
                accumulator += int(spl[1])
                currentIndex += 1
            elif spl[0] == 'jmp':
                currentIndex += int(spl[1])
        if currentIndex >= len(lines):
            print("--------------SUCCES: Accumulator: " + str(accumulator))
            break