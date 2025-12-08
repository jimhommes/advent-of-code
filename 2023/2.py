import numpy as np


with open('input/2.txt') as f:
    lines = f.readlines()

max_per_colour = {'red': 12, 'green': 13, 'blue': 14}


def test_blockset(bs):
    return bool(np.prod(np.array([v <= max_per_colour[k] for k, v in bs.items()])))

def get_maximums(bs):
    res = {'red': 0, 'green': 0, 'blue': 0}
    for k in res.keys():
        res[k] = max([[value for color, value in l.items() if color == k] for l in bs])[0]
    return res

total_ids = 0
total_powers = 0
for line in lines:
    game_id = int(line.split(':')[0].split(' ')[1])
    blocks = [{block_el.strip().split(' ')[1]: int(block_el.strip().split(' ')[0]) for block_el in blockset.split(',')} for blockset in line.split(':')[1].split(';')]
    tests = [test_blockset(blockset) for blockset in blocks]
    maximums = get_maximums(blocks)
    total_powers += np.prod(np.array(list(maximums.values())))

    if np.prod(np.array(tests)):
        total_ids += game_id

print(total_ids)
print(total_powers)
