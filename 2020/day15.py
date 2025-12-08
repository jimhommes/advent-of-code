with open('data/day15input', 'r') as myfile:
    lines = myfile.readlines()

starting_numbers = [int(x) for x in lines[0].split(",")]
#  Part 1

# numbers_spoken = []
#
# for i in range(5000):
#     if i < len(starting_numbers):
#         numbers_spoken.append(starting_numbers[i])
#     else:
#         most_recent = numbers_spoken[i-1]
#         if numbers_spoken.count(most_recent) == 1:
#             numbers_spoken.append(0)
#         else:
#             indices = [i for i, x in enumerate(numbers_spoken) if x == most_recent]
#             numbers_spoken.append(i - (indices[len(indices)-2]+1))
#
# print(numbers_spoken)

numbers_spoken = {}
previous_number = 0
current_number = 0
for i in range(30000000):
    if i < len(starting_numbers):
        current_number = starting_numbers[i]
    else:
        current_number = previous_number

    if current_number not in numbers_spoken.keys():
        new_number = 0
    else:
        new_number = i + 1 - numbers_spoken[current_number]

    numbers_spoken[current_number] = i + 1
    previous_number = new_number

print(current_number)