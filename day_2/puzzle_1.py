depth = 0
length = 0

# Read puzzle input
with open('puzzle_1_input.txt', 'r') as f:

  for line in f:
    # Instruction comes 1st, value 2nd
    instruction, value = line.split()
    value = int(value)

    if (instruction == 'up'):
      depth = depth - value
    elif (instruction == 'down'):
      depth = depth + value
    elif (instruction == 'forward'):
      length = length + value

print('distance: ' + str(length * depth))
