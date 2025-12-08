# Ideeen: apen parallelizeren
#
import math


class Monkey:
    def __init__(self, id, items, operation, test):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.amount_of_inspections = 0

    def __repr__(self):
        return 'Monkey ' + str(self.id) + ': ' + str(self.amount_of_inspections)


class Operation:
    def __init__(self, first_value, operator, second_value):
        self.first_value = first_value
        self.operator = operator
        self.second_value = second_value

    def calculate(self, old):
        if self.first_value == 'old':
            f = old
        else:
            f = int(self.first_value)
        if self.second_value == 'old':
            s = old
        else:
            s = int(self.second_value)

        if self.operator == '+':
            return f + s
        elif self.operator == '*':
            return f * s
        elif self.operator == '-':
            return f - s
        elif self.operator == '/':
            return f / s


class Test:
    def __init__(self, diviser, to_monkey_if_true, to_monkey_if_false):
        self.diviser = diviser
        self.to_monkey_if_true = to_monkey_if_true
        self.to_monkey_if_false = to_monkey_if_false

    def get_monkey_to(self, val):
        if val % self.diviser == 0:
            # print(str(val) + ' is divisible by ' + str(self.diviser))
            return self.to_monkey_if_true
        else:
            # print(str(val) + ' is not divisible by ' + str(self.diviser))
            return self.to_monkey_if_false


class Item:
    def __init__(self, start_value):
        self.start_value = start_value
        self.current_value = {}

    def calculate_for_divisers(self, divisers):
        for diviser in divisers:
            self.current_value[diviser] = self.start_value % diviser

    def calculate_operation(self, op):
        for diviser, value in self.current_value.items():
            self.current_value[diviser] = op.calculate(value) % diviser


def remove_comma(inp):
    if inp[-1] == ',':
        return inp[:(len(inp)-1)]
    else:
        return inp


with open('input/11.txt') as f:
    lines = f.readlines()

# Preprocessing
monkeys = []
all_divisers = []
for i in range(0, len(lines), 7):
    # Line 1
    monkey_line_split = lines[i].strip().split(' ')
    current_id = int(monkey_line_split[1][:(len(monkey_line_split[1])-1)])

    # Line 2
    starting_line_split = lines[i+1].strip().split(' ')
    current_items = [Item(int(remove_comma(i))) for i in starting_line_split[2:]]

    # Line 3
    operation_line_split = lines[i+2].strip().split(' ')
    current_operation = Operation(operation_line_split[3], operation_line_split[4], operation_line_split[5])

    # Line 4
    test_line_split = lines[i+3].strip().split(' ')
    all_divisers.append(int(test_line_split[3]))
    current_test = int(test_line_split[3])

    # Line 5
    true_line_split = lines[i+4].strip().split(' ')
    current_true = int(true_line_split[5])

    # Line 6
    false_line_split = lines[i+5].strip().split(' ')
    current_false = int(false_line_split[5])

    monkeys.append(Monkey(current_id, current_items, current_operation,
                          Test(current_test, current_true, current_false)))

# Init items
for items in [i.items for i in monkeys]:
    for item in items:
        item.calculate_for_divisers(all_divisers)

print(monkeys)
# rounds = 20 # Pt 1
rounds = 10000 # Pt 1

for round_count in range(1, rounds + 1):
    if round_count in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        print('Round ' + str(round_count))
        print(monkeys)
    for monkey in monkeys:
        for item in monkey.items:
            monkey.amount_of_inspections += 1
            # print('Monkey ' + str(monkey.id) + ' inspects ' + str(item))
            # after_operation = math.floor(monkey.operation.calculate(item) / 3) # Pt 1
            item.calculate_operation(monkey.operation)  # Pt 2
            # print('New value of item is ' + str(after_operation))
            to_monkey = monkey.test.get_monkey_to(item.current_value[monkey.test.diviser])
            # print('Item thrown to monkey ' + str(to_monkey))
            monkeys[to_monkey].items.append(item)
        monkey.items = []

amount_of_inspections_list = [i.amount_of_inspections for i in monkeys]
amount_of_inspections_list.sort(reverse=True)
print(math.prod(amount_of_inspections_list[:2]))

