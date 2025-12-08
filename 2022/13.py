import json
import functools

with open('input/13.txt') as f:
    lines = f.readlines()


def compare(el1, el2, prefix=''):
    print(prefix + '- Compare ' + str(el1) + ' vs. ' + str(el2))
    if type(el1) is int and type(el2) is int:
        # Both are integers
        if el1 == el2:
            print(prefix + '- Both integers match, continue')
            return 0
        else:
            print(prefix + '- Both integers differ, return ' + str(el1 < el2))
            if el1 < el2:
                return -1
            else:
                return 1

    elif type(el1) is list and type(el2) is list:
        # Both are lists
        left_smaller = len(el1) < len(el2)
        left_equals = len(el1) == len(el2)
        smallest_length = min([len(el1), len(el2)])
        for el_index in range(smallest_length):
            comp = compare(el1[el_index], el2[el_index], prefix + '  ')
            if comp != 0:
                print(prefix + '- Element returned ' + str(comp))
                return comp
        if left_equals:
            print(prefix + '- Lists ran out of elements, same length, continue')
            return 0
        else:
            print(prefix + '- List ran out of elements, return ' + str(left_smaller))
            if left_smaller:
                return -1
            else:
                return 1

    elif type(el1) is int:
        return compare([el1], el2, prefix + '  ')
    elif type(el2) is int:
        return compare(el1, [el2], prefix + '  ')


OK = []
NOK = []
pair_index = 0
pairs = []
for i in range(0, len(lines), 3):
    pair_index += 1
    print('== Pair ' + str(pair_index) + ' ==')
    pt1 = json.loads(lines[i])
    pt2 = json.loads(lines[i+1])
    outer_comp = compare(pt1, pt2)
    pairs.append(pt1)
    pairs.append(pt2)
    if outer_comp == 1 or outer_comp == 0:
        print('== Pair is NOK ==')
        NOK.append(pair_index)
    else:
        print('== Pair is OK ==')
        OK.append(pair_index)
    print('')

print(sum(OK))

# Part 2
pairs.append([[2]])
pairs.append([[6]])
pairs = sorted(pairs, key=functools.cmp_to_key(compare))
print(pairs)
print((pairs.index([[6]])+1) * (pairs.index([[2]])+1))
