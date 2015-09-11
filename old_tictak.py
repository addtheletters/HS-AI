# Tic tac toe learning?
#       Ben Zhang       
#       Period 2

#     



def blankBoard():
  return bo * 9

def stringBoard(perm, limit):
  newBoard = blankBoard()
  for n in range(limit+1):
    if n%2 == 0:
      newBoard = putIn(newBoard, perm.index(n), c1)
    else:
      newBoard = putIn(newBoard, perm.index(n), c2)
  return newBoard

def putIn(board, pos, char):
  return board[:pos] + char + board[pos+1:]

def isOver( board ):
  #if board.count(bo) < 2:
   # return True
  #if board.count(c1) > 4:
   # return True
  #if board.count(c2) > 4:
   # return True
  if hasWon(board, c1) or hasWon(board, c2):
    return True
  return False

def hasRow(board, char):
  for x in [0, 3, 6]:
    rowWin = True
    for y in [0, 1, 2]:
      if board[x+y] != char:
        rowWin = False
    if rowWin:
      return True
  return False

def hasCol(board, char):
  for x in [0, 1, 2]:
    colWin = True
    for y in [0, 3, 6]:
      if board[x+y] != char:
        colWin = False
    if colWin:
      return True
  return False

def hasDiag(board, char):
  # 0, 4, 8
  # 2, 4, 6
  if board[0] == char and board[4] == char and board[8] == char:
    return True
  if board[2] == char and board[4] == char and board[6] == char:
    return True
  return False
  
  '''
  for ind in [0, 4, 8]:
    diagWin = True
    if board[ind] != char:
      diagWin = False
    if diagWin:
      return True
  for ind in [2, 4, 6]:
    diagWin = True
    if board[ind] != char:
      diagWin = False
    if diagWin:
      return True
  return False
'''


def hasWon(board, char):
  if hasCol(board, char):
    #print( 'column win.' )
    return True
  if hasRow(board, char):
    #print( 'row win.' )
    return True
  if hasDiag(board, char):
    #print( 'diagonal win.')
    return True
  return False

def printBoard(board):
  print('<---------->')
  print( board[0], board[1], board[2] )
  print( board[3], board[4], board[5] )
  print( board[6], board[7], board[8] )
  if hasWon(board, c1):
    print(c1 + ' has won.')
  if hasWon(board, c2):
    print(c2 + ' has won.')
  if isOver(board):
    print('Game is over.')

  
sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8,]
from itertools import permutations
filledBoards = list(permutations(sequence, 9))

bo = '-'
c1 = 'X'
c2 = 'O'

dataBase = {}

print(len(filledBoards))

#testcase = '--O-X-O--'
#print(hasWon(testcase, 'O'))

dataBase['---------'] = 0

for perm in filledBoards:
  for lim in range(0, 8):
    brd = stringBoard(perm, lim)
    #printBoard(brd)
    if not isOver(brd):
      dataBase[brd] = 0



print(dataBase)
print('length:', len(dataBase))


