
with open('data/day2passwords', 'r') as myfile:
    lines = myfile.readlines()

amountValid = 0

for line in lines:
    spl = line.split(" ")
    limits = spl[0].split("-")
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])
    letter = spl[1].split(":")[0]
    password = spl[2]
    # if lower_limit <= password.count(letter) <= upper_limit:
    #     amountValid += 1
    if bool(password[lower_limit - 1] == letter) != bool(password[upper_limit - 1] == letter):
        amountValid += 1

print(amountValid)
