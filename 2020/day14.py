with open('data/day14input', 'r') as myfile:
    lines = myfile.readlines()


def to_bit_string(startdec, length):
    res = []
    currentdec = startdec
    for i in reversed(range(length+1)):
        if 2**i <= currentdec:
            currentdec -= 2**i
            res.append('1')
        else:
            res.append('0')
    return "".join(res)


def mask_bit_string(msk, str):
    msklst = list(msk)
    strlst = list(str)
    res = []
    for i in range(len(msklst)):
        if msklst[i] == 'X':
            res.append(strlst[i])
        else:
            res.append(msklst[i])
    return "".join(res)


def to_decimal(str):
    strlst = list(reversed(list(str)))
    dec = 0
    for i in range(len(strlst)):
        dec += int(strlst[i]) * 2 ** i
    return dec


mem = dict()
mask = ''

for line in lines:
    spl = line.split(" = ")
    if spl[0] == 'mask':
        mask = spl[1]
    else:
        bitstr = to_bit_string(int(spl[1]), 36)
        maskedbitstr = mask_bit_string(mask, bitstr)
        mem[int(spl[0].split("[")[1].split("]")[0])] = maskedbitstr

sum = 0
for val in mem.values():
    sum += to_decimal(val.strip())

print(sum)


def mask_bit_string_v2(msk, str):
    msklst = list(msk)
    strlst = list(str)
    res = []
    for i in range(len(msklst)):
        if msklst[i] == '0':
            res.append(strlst[i])
        else:
            res.append(msklst[i])
    return "".join(res)


def to_list_of_bit_strings(amount, msk):
    res = []
    for i in range(2 ** amount):
        res.append(list(to_bit_string(i, amount-1)))
    for i in range(2 ** amount):
        subres = msk
        for repl in res[i]:
            subres = subres.replace('X', repl, 1)
        res[i] = subres
    return res


def to_indices(msk, dec):
    bitstr = to_bit_string(int(dec), 35)
    msk = mask_bit_string_v2(msk, bitstr)
    listofmasks = to_list_of_bit_strings(msk.count('X'), msk)
    # res = []
    # for lstmsk in listofmasks:
    #     res.append(mask_bit_string_v2(lstmsk, bitstr))
    # print(res)
    return [to_decimal(x) for x in listofmasks]


mem = dict()
mask = ''

for line in lines:
    spl = line.split(" = ")
    if spl[0] == 'mask':
        mask = spl[1].strip()
    else:
        for i in to_indices(mask.strip(), int(spl[0].split("[")[1].split("]")[0])):
            mem[i] = int(spl[1].strip())


sum = 0
for val in mem.values():
    sum += int(val)

print(sum)