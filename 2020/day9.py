
from numpy import long

with open('data/day9input', 'r') as myfile:
    lines = myfile.readlines()


def combinationExists(preamble, toCombine):
    res = False
    for i_inner in range(len(preamble)-1):
        for j in range(i_inner+1, len(preamble)):
            if preamble[i_inner] + preamble[j] == toCombine:
                res = True
                break
        if res:
            break

    return res


preambleLength = 25
notPossible = -1
preamble = []
for i in range(preambleLength, len(lines)):
    print("Index: " + str(i) + ": " + lines[i].strip())
    preamble = [long(x) for x in lines[i-preambleLength:i]]
    print(preamble)
    if not combinationExists(preamble, long(lines[i])):
        notPossible = long(lines[i])
        break

print(notPossible)
print("")
print("Preamble " + str(preamble))

for combinationSize in range(2, len(lines)+1):
    end = False
    for i in range(len(lines)-combinationSize):
        # print("Checking from " + str(i) + " to " + str(i+combinationSize))
        # print(lines[i:i+combinationSize])
        combination = [long(x) for x in lines[i:i+combinationSize]]
        if sum(combination) == notPossible:
            print(str(min(combination)) + " " + str(max(combination)))
            print(min(combination) + max(combination))
            end = True
            break
        else:
            print(str(sum(combination)) + " != " + str(notPossible))

    if end:
        break

print(end)