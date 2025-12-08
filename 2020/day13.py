with open('data/day13input', 'r') as myfile:
    lines = myfile.readlines()

start = int(lines[0])
busids = [int(x) for x in list(filter(('x').__ne__, lines[1].split(',')))]
iterations = 100

for timestamp in range(start, start+iterations):
    end = False
    for busid in busids:
        if timestamp % busid == 0:
            print((timestamp - start) * busid)
            end = True
            break
    if end:
        break

busids = lines[1].split(",")
t = int(busids[0])
mod = 0
mult = t
start = 0

for offset in range(1, len(busids)):
    if busids[offset] != 'x':
        x = t
        for m in range(2, 1000000):
            if (x+offset) % int(busids[offset]) == 0:
                mod = t = x
                mult *= int(busids[offset])
                start = t
                break
            else:
                x = start + m * mult
print(t)