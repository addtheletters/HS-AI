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
  #if hasWon(board, c1):
   # print(c1 + ' has won.')
  #if hasWon(board, c2):
   # print(c2 + ' has won.')
  if isOver(board):
    print('Game is over.')

def generateBoardPermutations():
  sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8,]
  from itertools import permutations
  filledBoards = list(permutations(sequence, 9))
  return filledBoards
  
def blankDatabaseValue():
  return ([9] * 9)# + [-1]
  
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
  movesMade0 = []
  movesMade1 = []
  
  while canPlay(currentBoard) and (not ( hasWon(currentBoard, c1) or hasWon(currentBoard, c2)) ):
    try:
      move = chooseMove( currentBoard, dataBase )
    except IndexError:
      print('error choosing move for board')
      printBoard(currentBoard)
      print(dataBase[currentBoard])
      confirm = input("Please confirm: ")
      return
    #print("Making move.", "Board is", currentBoard, "move is", move, "player is", playerChars[currentPlayer])
    if currentPlayer == 0:
      movesMade0.append( [currentBoard, move] )
    else:
      movesMade1.append( [currentBoard, move] )
    currentBoard = putIn( currentBoard, move, playerChars[currentPlayer] )
    currentPlayer += 1
    if currentPlayer >= 2:
      currentPlayer = 0
  if hasWon(currentBoard, c1):
    #print("Player of character", c1, "won!")
    amendDatabaseProbabilities(dataBase, movesMade0, WIN)
    amendDatabaseProbabilities(dataBase, movesMade1, LOSS)
    return
  if hasWon(currentBoard, c2):
    #print("Player of character", c2, "(the computer) won!")
    amendDatabaseProbabilities(dataBase, movesMade0, LOSS)
    amendDatabaseProbabilities(dataBase, movesMade1, WIN)
    return
  #print("Draw.")
  amendDatabaseProbabilities(dataBase, movesMade0, TIE)
  amendDatabaseProbabilities(dataBase, movesMade1, TIE)

def validMoveStrings(board):
  outr = []
  for ind in range(len(board)):
    if board[ind] == bo:
      outr.append( str(ind) )
  return outr

def getHumanMove(board):
  printBoard(board)
  printBoard("012345678")
  while True:
    print("'k' to exit.")
    choice = input("Move? ")
    if choice in validMoveStrings(board):#['0', '1', '2', '3', '4', '5', '6', '7', '8']:
      return int(choice)
    elif choice == 'k':
      exit()
    else:
      print("Invalid!")
    
def playHumanGame( dataBase ):
  currentBoard = blankBoard()
  currentPlayer = 0
  movesMade0 = []
  movesMade1 = []
  
  while canPlay(currentBoard) and (not ( hasWon(currentBoard, c1) or hasWon(currentBoard, c2)) ):
    if currentPlayer != 0:
      move = chooseBestMove( currentBoard, dataBase )
      movesMade0.append( [currentBoard, move] )
      currentBoard = putIn( currentBoard, move, playerChars[currentPlayer] )
    else:
      move = getHumanMove(currentBoard)
      movesMade1.append( [currentBoard, move] )
      currentBoard = putIn( currentBoard, move, playerChars[currentPlayer] )
    currentPlayer += 1
    if currentPlayer >= 2:
      currentPlayer = 0
  
  printBoard(currentBoard)
  if hasWon(currentBoard, c1):
    print("Player of character", c1, "won!")
    #amendDatabaseProbabilities(dataBase, WIN)
    return
  if hasWon(currentBoard, c2):
    print("Player of character", c2, "(the computer) won!")
    #amendDatabaseProbabilities(dataBase, LOSS)
    return
  print("Draw.")
  #amendDatabaseProbabilities(dataBase, TIE)
  return


def getAdjustedChances( board, dataBase ): #prevents choosing of already taken spaces
  chances = (dataBase[board])[:]
  for ind in range(len(board)):
    if board[ind] != bo:
      chances[ind] = 0
  return chances
import random

def randomPossibleMove(board):
  possible = []
  for ind in range(len(board)):
    if board[ind] == bo:
      possible.append(ind)
  return random.choice(possible)

def chooseBestMove( board, dataBase ):
  ch = getAdjustedChances(board, dataBase)
  if sum(ch) < 1:
    return randomPossibleMove(board)
  return ch.index( max(ch) )
  
def chooseMove( board, dataBase ):
  ch = getAdjustedChances(board, dataBase)
  if sum(ch) < 1:
    return randomPossibleMove(board)
  chosen = weightedRandom( ch )
  #dataBase[board][9] = chosen
  return chosen

  
def weightedRandom( lst ):
  chooser = []
  for ind in range(len(lst)):
    chooser += (lst[ind] * [ind])
  return random.choice(chooser)
  

WIN = 3
TIE = 1
LOSS = -1

def amendDatabaseProbabilities( dataBase, moves, state ):
  for move in moves:
    if (not canPlay(move[0])) or hasWon(move[0], c1) or hasWon(move[0], c2):
      continue
    dataBase[move[0]][move[1]] += state
  '''for key in dataBase:
    chosenMove = dataBase[key][9]
    if chosenMove == -1: #no move taken
      continue
    dataBase[key][chosenMove] += state'''
  #print('Database amended with state', state)


import json

def saveDataBaseToFile( dataBase, filename ):
  f = open(filename, 'w')
  json.dump(dataBase, f)
  f.close()
  return

def loadDataBaseFromFile( filename ):
  f = open(filename)
  data = json.load(f)
  f.close()
  return data

def main():

  whatdo = input("Enter 'g' to generate new database, or anything else to use from file: ")
  filenom = 'data.txt'
  dataBase = {}
  
  if whatdo == 'g':
    dataBase = fillDatabase(generateBoardPermutations())
    print("Filled database.")
    print('length:', len(dataBase))
  else:
    dataBase = loadDataBaseFromFile(filenom)
  
  print("'h' for human game")
  print("'w' to save database to file")
  print("'k' to kill")
  print("'t' to train")
  
  while True:
    gogo = input("? ")
    if gogo == 'help':
      print("'h' for human game")
      print("'w' to save database to file")
      print("'k' to kill")
      print("'t' to train")
    elif gogo == 'h':
      print('playing human game')
      playHumanGame(dataBase)
    elif gogo == 'w':
      confirm = input('Are you sure? Will overwrite previously stored datafile. "yes" to confirm: ')
      if confirm == 'yes':
        print('writing...')
        saveDataBaseToFile(dataBase, filenom)
        print('done!')
      else:
        print('write cancelled.')
    elif gogo == 'k':
      print('exiting')
      exit()
    elif gogo == 't':
      games = 1
      inning = input("How much training? ")
      try:
        games = int(inning)
      except Exception:
        print("unable to parse int")
      for x in range(games):
        #print("Playing training game", x)
        playTrainingGame(dataBase)
      print("Training", games, "times completed.")
    elif gogo == 'ti':
      times = 0
      games = 5000
      while True:
        times += 1
        for x in range(games):
          playTrainingGame(dataBase)
        print('trained a bit, saving', times)
        saveDataBaseToFile(dataBase, filenom)
    else:
      print('unrecognized')
      #playTrainingGame(dataBase)
      
  
  


bo = '-'
c1 = 'X'
c2 = 'O'

playerChars = {}
playerChars[0] = c1
playerChars[1] = c2

if __name__ == '__main__': main();

