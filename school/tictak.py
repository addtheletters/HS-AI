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

def canPlay(board):
  return (board.count(bo) > 0)

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

def generateBoardPermutations():
  sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8,]
  from itertools import permutations
  filledBoards = list(permutations(sequence, 9))
  return filledBoards
  
def blankDatabaseValue():
  return ([9] * 9) + [-1]
  
def fillDatabase( boardPermutations ):
  dataBase = {}
  dataBase['---------'] = blankDatabaseValue()
  for perm in boardPermutations:
    for lim in range(0, 8):
      brd = stringBoard(perm, lim)
      #printBoard(brd)
      if not isOver(brd):
        dataBase[brd] = blankDatabaseValue()
  return dataBase


def playTrainingGame( dataBase ):
  currentBoard = blankBoard()
  currentPlayer = 0
  while canPlay(currentBoard) and (not ( hasWon(currentBoard, c1) or hasWon(currentBoard, c2)) ):
    move = chooseMove( currentBoard, dataBase )
    putIn( currentBoard, move, playerChars[currentPlayer] )
    currentPlayer += 1
    if currentPlayer >= 2:
      currentPlayer = 0
  if hasWon(currentBoard, c1):
    print("Player of character", c1, "won!")
    amendDatabaseProbabilities(dataBase, WIN)
    return
  if hasWon(currentBoard, c2):
    print("Player of character", c2, "(the computer, kindof) won!")
    amendDatabaseProbabilities(dataBase, LOSS)
    return
  print("Draw.")
  amendDatabaseProbabilities(dataBase, TIE)
    
def getHumanMove(board):
  printBoard(board)
  printBoard("012345678")
  while True:
    choice = input("Move?")
    if ['0', '1', '2', '3', '4', '5', '6', '7', '8'].contains(choice):
      return choice
    
def playHumanGame( dataBase ):
  currentBoard = blankBoard()
  currentPlayer = 0
  while canPlay(currentBoard) and (not ( hasWon(currentBoard, c1) or hasWon(currentBoard, c2)) ):
    if currentPlayer != 0:
      move = chooseMove( currentBoard, dataBase )
      putIn( currentBoard, move, playerChars[currentPlayer] )
    else:
      move = getHumanMove(currentBoard)
      putIn( currentBoard, move, playerChars[currentPlayer] )
    currentPlayer += 1
    if currentPlayer >= 2:
      currentPlayer = 0
  if hasWon(currentBoard, c1):
    print("Player of character", c1, "won!")
    amendDatabaseProbabilities(dataBase, WIN)
    return
  if hasWon(currentBoard, c2):
    print("Player of character", c2, "(the computer, kindof) won!")
    amendDatabaseProbabilities(dataBase, LOSS)
    return
  print("Draw.")
  amendDatabaseProbabilities(dataBase, TIE)


def chooseMove( board, dataBase ):
  probabilities = dataBase[board][:-1]
  chosen = weightedRandom( probabilities )
  dataBase[board][9] = chosen
  return chosen
  
import random
  
def weightedRandom( lst ):
  chooser = []
  for ind in range(len(lst)):
    chooser += (lst[ind] * [ind])
  return random.choice(chooser)
  

WIN = 3
TIE = 1
LOSS = -1

def amendDatabaseProbabilities( dataBase, state ):
  for key in dataBase:
    chosenMove = dataBase[key][9]
    if chosenMove == -1: #no move taken
      continue
    dataBase[key][chosenMove] += state
  print('Database amended with state', state)
    

def main():
  dataBase = fillDatabase(generateBoardPermutations())
  
  for x in range(1000):
    playTrainingGame(dataBase)
  
  while True:
    gogo = input()
    if gogo == 't':
      playTrainingGame(dataBase)
    elif gogo == 'k':
      exit()
    else:
      playHumanGame(dataBase)
      
   
  
  playTrainingGame(dataBase)
  
  print('length:', len(dataBase))


bo = '-'
c1 = 'X'
c2 = 'O'

playerChars = {}
playerChars[0] = c1
playerChars[1] = c2

if __name__ == '__main__': main();

