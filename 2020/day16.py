with open('data/day16input', 'r') as myfile:
    lines = myfile.readlines()

conditions_lastline = lines.index("\n")
yourticket_lastline = conditions_lastline + lines[conditions_lastline+1:].index("\n") + 1

# Process conditions
conditions = []
for i in range(conditions_lastline):
    for condition in [x.strip() for x in lines[i].split(" ") if '-' in x]:
        conditions.append((int(condition.split("-")[0]), int(condition.split("-")[1])))


# Process nearby tickets
invalid_numbers = []
valid_tickets = []
for nearby_ticket in lines[yourticket_lastline+2:]:
    numbers = [int(x) for x in nearby_ticket.strip().split(",")]
    ticket_valid = True
    for number in numbers:
        number_invalid = True
        for condition in conditions:
            if condition[0] <= number <= condition[1]:
                number_invalid = False
                break
        if number_invalid:
            ticket_valid = False
            invalid_numbers.append(number)
    if ticket_valid:
        valid_tickets.append(numbers)

# Print sum
print(sum(invalid_numbers))

# Part 2
print(valid_tickets)

# Reprocess conditions
conditions = {}
for i in range(conditions_lastline):
    key = lines[i].split(":")[0]
    conditions[key] = []
    for condition in [x.strip() for x in lines[i].split(" ") if '-' in x]:
        conditions[key].append((int(condition.split("-")[0]), int(condition.split("-")[1])))

# Check columns
solved_indices = {}
while len(conditions) > 1:
    for column in range(len(valid_tickets[0])):
        possible_conditions = conditions.copy()
        for row in range(len(valid_tickets)):
            for (key, all_conditions) in conditions.items():
                keep_condition = False
                for value in all_conditions:
                    checkval = valid_tickets[row][column]
                    if value[0] <= checkval <= value[1]:
                        keep_condition = True
                if not keep_condition:
                    if key in possible_conditions.keys():
                        possible_conditions.pop(key)
        # print(possible_conditions)
        if len(possible_conditions.keys()) == 1:
            solved_indices[list(possible_conditions.keys())[0]] = column
            conditions.pop(list(possible_conditions.keys())[0])

print(solved_indices)

your_ticket = [int(x) for x in lines[conditions_lastline+2].split(",")]

solution = 1
for key in solved_indices.keys():
    if "departure" in key:
        solution *= your_ticket[solved_indices[key]]

print(solution)
