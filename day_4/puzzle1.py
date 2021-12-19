answers = []

# Read puzzle input
with open('input.txt', 'r') as f:

  # Step through each line of inputs
  for line_num, data in enumerate(f):
    if line_num == 0:
      answers = [x.strip('\n') for x in data.split(',')]
    else:
      print([int(data[i:i+3].strip('\n').strip(' ')) for i in range(0, len(data), 3) if data is not '\n'])