import re

with open('input/3.txt') as f:
    lines = f.readlines()


class SchematicUnit:

    def __init__(self, v, x, y, ul):
        self.value = v
        self.x = x
        self.y = y
        self.length = ul
        self.neighbors = []
        self.symbol_adjacent = False

    def add_neighbor(self, nb):
        if nb not in self.neighbors and nb != self:
            self.neighbors.append(nb)
            if isinstance(self, Symbol) and isinstance(nb, Number):
                nb.symbol_adjacent = True
                print(str(self) + ' is a symbol! Neighbor ' + str(nb) + ' has been set to Symbol Adjacent')
        if isinstance(nb, Symbol) and isinstance(self, Number):
            self.symbol_adjacent = True
            print(str(nb) + ' is a symbol! Neighbor ' + str(self) + ' has been set to Symbol Adjacent')

    def __repr__(self):
        return str(self.value)


class Number(SchematicUnit):

    def __init__(self, v, x, y):
        SchematicUnit.__init__(self, v, x, y, len(str(v)))
        self.part_number = False


class Symbol(SchematicUnit):

    def __init__(self, v, x, y):
        SchematicUnit.__init__(self, v, x, y, 1)


class Schematic:

    def __init__(self, input_lines):
        self.schematic = [[None] * len(input_line.strip()) for input_line in input_lines]
        self.numbers = []
        self.symbols = []

    def enter_value(self, value):
        print('Entering value into schematic ' + str(value))
        # Fill in schematic
        for i in range(value.length):
            print('Entering ' + str(value) + ' into x: ' + str(value.x + i) + ', y: ' + str(value.y))
            self.schematic[value.y][value.x + i] = value

        # Find and add all neighbours
        print('Adding neighbors. Current ' + str(value) + ' neighbors: ' + str(value.neighbors))
        for neighb in self.get_all_adjacent_values(value.x, value.x + value.length, value.y):
            value.add_neighbor(neighb)
            neighb.add_neighbor(value)
        print('New value neighbors: ' + str(value.neighbors))

        # Add to according list
        if isinstance(value, Number):
            self.numbers.append(value)
        elif isinstance(value, Symbol):
            self.symbols.append(value)

    def get_all_adjacent_values(self, start_x, end_x, y):
        res = []
        min_x = start_x - 1 if start_x - 1 >= 0 else 0
        max_x = end_x + 1 if end_x + 1 <= len(self.schematic[0]) - 1 else len(self.schematic[0]) - 1
        min_y = y - 1 if y - 1 >= 0 else 0
        max_y = y + 1 if y + 1 <= len(self.schematic) - 1 else len(self.schematic) - 1
        for curr_y in range(min_y, max_y):
            res += self.schematic[curr_y][min_x:max_x]
        return [resel for resel in res if resel is not None]

    def __repr__(self):
        res = 'Current Schematic\n'
        for row in self.schematic:
            res += str(row) + '\n'
        return res


# Init schematic
schema = Schematic(lines)
# print(schema)

for i in range(len(lines)):
    line = lines[i]
    line_to_find = line
    for el in line.strip().split('.'):
        for digit in re.findall(r'\d+', el):
            print('Found digit ' + str(digit))
            schema.enter_value(Number(digit, line_to_find.find(digit), i))
            line_to_find = line_to_find.replace(digit, '.' * len(digit), 1)
        for symbol in re.findall(r'[^0-9]', el):
            print('Found symbol ' + str(symbol))
            schema.enter_value(Symbol(symbol, line_to_find.find(symbol), i))
            line_to_find = line_to_find.replace(symbol, '.', 1)

# print(schema)
print('')
print('The sum of all numbers that have a symbol adjacent: ' + str(sum([int(schemnum.value) for schemnum in schema.numbers if schemnum.symbol_adjacent])))

# print(schema)
list_of_gears = [schemsym.neighbors for schemsym in schema.symbols if schemsym.value == '*' and len(schemsym.neighbors) == 2]
print(list_of_gears)
list_of_gear_ratios = [int(gear[0].value) * int(gear[1].value) for gear in list_of_gears]
print(list_of_gear_ratios)
print('The multiplication of all * that have two numbers adjacent: ' + str(sum(list_of_gear_ratios)))
