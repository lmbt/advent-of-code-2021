import sys

def scanLineForWin(line, answers):
  count = 0
  for num in line:
    if num in answers:
      count = count + 1
  return count == 5

def scanRowsForWin(board, answers):
  for row in board:
    if scanLineForWin(row, answers):
      return True
  return False

def scanColsForWin(board, answers):
  for i in range(0, 5):
    if scanLineForWin([x[i] for x in board], answers):
      return True
  return False

def scanDiagsForWin(board, answers):
  if scanLineForWin([x[i] for i, x in enumerate(board)], answers):
    return True
  if scanLineForWin([x[4-i] for i, x in enumerate(board)], answers):
    return True
  return False

def checkBoardForWin(board, answers):
  if scanRowsForWin(board, answers):
    return True
  if scanColsForWin(board, answers):
    return True
  # DIAGONALS DONT COUNT
  #if scanDiagsForWin(board, answers):
  #  return True
  return False

def calculateScore(board, answers):
  score = 0
  for row in board:
    for num in row:
      if num not in answers:
        score = score + num
  return score * answers[-1]

if __name__ == '__main__':
  answers = []
  boards = []
  counter = -1

  # Read puzzle input
  with open('input.txt', 'r') as f:
    # Step through each line of inputs
    for line_num, data in enumerate(f):
      if line_num == 0:
        answers = [int(x.strip('\n')) for x in data.split(',')]
      else:
        split_data = [int(data[i:i+3].strip('\n').strip(' ')) for i in range(0, len(data), 3) if data != '\n']
        if split_data == []:
          # create new puzzle board
          boards.append([])
          counter = counter + 1
        else:
          # extend current puzzle board
          boards[counter].append(split_data)

  ignored_boards = []
  # Make a new answer available each cycle
  for i in range(0, len(answers)):
    # Check all combinations of all boards to see if any are winners
    for b in range(0, len(boards)):
      board = boards[b]
      ans = answers[0:i]
      if checkBoardForWin(board, ans):
        if b not in ignored_boards:
          if len(ignored_boards) == len(boards) - 1:
            # Found last board
            print('Last winning board: ' + str(b))
            print('score is: ' + str(calculateScore(board, ans)))
            sys.exit(0)
          else:
            ignored_boards.append(b)

