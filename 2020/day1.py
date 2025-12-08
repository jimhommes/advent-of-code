
data = []

with open('data/day1input', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    data.append(int(line))

for i in range(len(data) - 2):
    for j in range(i, len(data) - 1):
        for k in range(j, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(str(data[i]) + ", " + str(data[j]) + ", " + str(data[k]) + ", " + str(data[i] * data[j] * data[k]))