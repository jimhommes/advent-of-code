import re

with open('data/day4passwords', 'r') as myfile:
    lines = myfile.readlines()

currentFields = []
currentValues = []
amountValid = 0

byrchecked = False
iyrchecked = False
eyrchecked = False
hgtchecked = False
hclchecked = False
eclchecked = False
pidchecked = False

for line in lines:
    # print(line)
    if line == '\n':
        # Controleer alle velden in currentFields
        for i in range(len(currentFields)):
            cf = currentFields[i].strip()
            cv = currentValues[i].strip()

            if cf == 'byr':
                byrchecked = 1920 <= int(cv) <= 2002
                print("byrchecked: " + str(cv) + ", " + str(byrchecked))
            if cf == 'iyr':
                iyrchecked = 2010 <= int(cv) <= 2020
                print("iyrchecked: " + str(cv) + ", " + str(iyrchecked))
            if cf == 'eyr':
                eyrchecked = 2020 <= int(cv) <= 2030
                print("eyrchecked: " + str(cv) + ", " + str(eyrchecked))
            if cf == 'hgt':
                if "cm" in cv:
                    hgtchecked = 150 <= int(cv.split("cm")[0]) <= 193
                if "in" in cv:
                    hgtchecked = 59 <= int(cv.split("in")[0]) <= 76
                print("hgtchecked: " + str(cv) + ", " + str(hgtchecked))
            if cf == 'hcl':
                reg = re.compile('^#(?:[0-9a-fA-F]{3}){1,2}$')
                hclchecked = (reg.match(cv) is not None)
                print("hclchecked: " + str(cv) + ", " + str(hclchecked))
            if cf == 'ecl':
                eclchecked = cv == 'amb' or cv == 'blu' or cv == 'brn' or cv == 'gry' or cv == 'grn' or cv == 'hzl' or cv == 'oth'
                print("eclchecked: " + str(cv) + ", " + str(eclchecked))
            if cf == 'pid':
                pidchecked = len(cv) == 9
                print("pidchecked: " + str(cv) + ", " + str(pidchecked))

        if byrchecked and iyrchecked and eyrchecked and hgtchecked and hclchecked and eclchecked and pidchecked:
            amountValid += 1

        byrchecked = False
        iyrchecked = False
        eyrchecked = False
        hgtchecked = False
        hclchecked = False
        eclchecked = False
        pidchecked = False
        currentFields = []
        currentValues = []
    else:
        for part in line.split(" "):
            currentFields.append(part.split(":")[0])
            currentValues.append(part.split(":")[1])

print(amountValid)