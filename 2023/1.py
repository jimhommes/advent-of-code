import re

numbers_text_to_digit = {'one': '1', 'two': '2', 'three': '3.txt', 'four': '4', 'five': '5',
                         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

with open('input/1.txt') as f:
    lines = f.readlines()

digits = []
digit_strings = []
for line in lines:
    print('Line found: ' + line.strip())
    line_pretreated = line.strip()
    to_find = list(numbers_text_to_digit.keys()) + list(numbers_text_to_digit.values())
    indices = {}
    for k in to_find:
        for l in [m.start() for m in re.finditer(k, line_pretreated)]:
            if k in numbers_text_to_digit.keys():
                indices[l] = numbers_text_to_digit[k]
            else:
                indices[l] = k

    indices = dict(sorted(indices.items()))
    print(indices)

    digit = list(indices.values())
    digits.append(int(digit[0] + digit[-1]))
    print('Final number: ' + str(digits[-1]))


print(sum(digits))

