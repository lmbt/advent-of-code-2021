# Rounding :)
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

# Get oxygen generator rating (made of most common bits)
def oxygenRating(bit_strings):

  offset = 0
  while len(bit_strings) > 1:
    bit_val = findMostCommonBit(bit_strings, offset)
    bit_strings = filterBitStrings(bit_strings, str(bit_val), offset)
    offset = offset + 1
  
  return bit_strings[0]

# Get co2 scrubber rating (made of least common bits)
def co2Rating(bit_strings):

  offset = 0
  while len(bit_strings) > 1:
    bit_val = int(not findMostCommonBit(bit_strings, offset))
    bit_strings = filterBitStrings(bit_strings, str(bit_val), offset)
    offset = offset + 1

  return bit_strings[0]

# Find most common bit through the list for specified position
def findMostCommonBit(input_list, offset=0):
  total = 0
  line_count = 0
  for item in input_list:
    total = total + int(item[offset])
    line_count = line_count + 1
  return decimal.Decimal(total / line_count).to_integral_value()

def filterBitStrings(input_list, value, offset=0):
  return [x for x in input_list if x[offset] == value]

if __name__ == '__main__':
  bit_strings = []

  # Read puzzle input and store list of bit strings
  with open('puzzle_input.txt', 'r') as f:
    for line in f:
      # Strip newline character if it exists
      bit_strings.append(line[:-1] if line[-1] == '\n' else line)

  oxygen = oxygenRating(bit_strings)
  co2 = co2Rating(bit_strings)

  # Multiply oxygen rating and co2 rating to get solution
  print('solution: ' + str(int(oxygen, 2) * int(co2, 2)))

