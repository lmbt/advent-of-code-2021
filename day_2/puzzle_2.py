aim = 0
sub_x = 0
sub_y = 0

# Read puzzle input
with open('puzzle_1_input.txt', 'r') as f:

  for line in f:
    # Instruction comes 1st, value 2nd
    instruction, value = line.split()
    value = int(value)

    if (instruction == 'up'):
      aim = aim - value
    elif (instruction == 'down'):
      aim = aim + value
    elif (instruction == 'forward'):
      sub_x = sub_x + value
      sub_y = sub_y + (aim * value)

print('sub_x: ' + str(sub_x))
print('sub_y: ' + str(sub_y))
print('answer: ' + str(sub_x * sub_y))