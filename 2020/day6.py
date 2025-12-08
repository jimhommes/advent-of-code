
with open('data/day6input', 'r') as myfile:
    lines = myfile.readlines()

# Part 1
# amountOfYes = 0
# answeredYes = []
#
# for line in lines:
#     print(line.strip())
#     if line == '\n':
#         amountOfYes += len(answeredYes)
#         print(len(answeredYes))
#         print(amountOfYes)
#         answeredYes = []
#     else:
#         for char in line.strip():
#             if char not in answeredYes:
#                 answeredYes.append(char)
#         answeredYes.sort()
#         print(answeredYes)
#
# amountOfYes += len(answeredYes)
# print(len(answeredYes))
# print(amountOfYes)
# answeredYes = []
# print(amountOfYes)

# Part 2
currentSelection = list('abcdefghijklmnopqrstuvwxyz')
listToRemove = []
amountOfYes = 0

for line in lines:
    print(line.strip())
    if line == '\n':
        amountOfYes += len(currentSelection)
        currentSelection = list('abcdefghijklmnopqrstuvwxyz')
    else:
        for char in currentSelection:
            print(char)
            if char not in line:
                print('removed')
                listToRemove.append(char)
        for char in listToRemove:
            currentSelection.remove(char)
        listToRemove = []
        print(currentSelection)

amountOfYes += len(currentSelection)
print(amountOfYes)