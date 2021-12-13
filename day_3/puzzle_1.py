# Rounding :)
import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

bits = {}

lines = 0

# Read puzzle input
with open('puzzle_input.txt', 'r') as f:

  # Step through each line of inputs
  for line in f:
    # Assign values to proper buckets
    for index, value in enumerate(line):
      if (value != '\n'):
        if index not in bits:
          bits[index] = 0
        bits[index] = bits[index] + int(value)
    lines = lines + 1

# Average the bits
for index, value in enumerate(bits):
  bits[index] = decimal.Decimal(bits[index] / lines).to_integral_value()

gamma_binary = ''
for bit in bits:
  gamma_binary = gamma_binary + str(bits[bit])
gamma_decimal = int(gamma_binary, 2)

epsilon_binary = ''
for bit in bits:
  epsilon_binary = epsilon_binary + str(int(not bits[bit]))
epsilon_decimal = int(epsilon_binary, 2)

print('gamma rate: ')
print(' - binary: ' + gamma_binary)
print(' - decimal: ' + str(gamma_decimal))

print('epsilon rate: ')
print(' - binary: ' + epsilon_binary)
print(' - decimal: ' + str(epsilon_decimal))

print('solution: ' + str((gamma_decimal * epsilon_decimal)))