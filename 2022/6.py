
with open('input/6.txt') as f:
    lines = f.readlines()
    puzzle_input = lines[0]

print('Puzzle input: ' + puzzle_input)


def find_marker(inp, length):
    for i in range(len(inp) - length):
        curr_str = inp[i:i+length]
        if all_unique_chars(curr_str):
            print('Marker found with the arrival of char no ' + str(i+length))
            return curr_str


def all_unique_chars(inp):
    for char in inp:
        if inp.count(char) > 1:
            return False
    return True


marker = find_marker(puzzle_input, 4)
print('Marker: ' + marker)

marker = find_marker(puzzle_input, 14)
print('Marker: ' + marker)
