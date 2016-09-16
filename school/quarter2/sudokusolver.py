### Ben Zhang
### Sudoku Solver
### 10-22-13

class Cell(object):
  matrix = None
  
  def __init__(self, val, r, c, matrix):
    if val == 0:
      self.value = set(range(1, MAX+1))
      self.wasInitial = False
    else:
      self.value = {val,}
      self.wasInitial = True
    self.row = r
    self.col = c
    self.block = self.blockNumber(r, c)
	
    Cell.matrix = matrix
	
  def __repr__(self):
    if len(self.value) == 1:
      element = str(list(self.value)[0])
    else:
      element = ' '
    return element
  
  def print(matrix, details = False):
    print('+---' * MAX + '+')
    for r in range(MAX):
      for c in range(MAX):
        if len(Cell.matrix[r][c].value) == 1:
          elt = list(Cell.matrix[r][c].value)[0]
          print('| ',elt,' ',end = '', sep = '')
        else: print('|  ', end = '', sep = '')
      print('|')
      print('+---' * MAX + '+')
    print()
    if details == True:
      for r in range(MAX):
        for c in range(MAX):
          print('matrix[', r, '][', c, '].value =', matrix[r][c].value, sep = '')
        print()

  def blockNumber(self, row, col):
    if (self.row < 3) and (self.col< 3): return 0
    if (self.row < 3) and (2 < self.col<6): return 1
    if (self.row < 3) and (5 < self.col): return 2
    if (2 < self.row < 6) and (self.col < 3): return 3
    if (2 < self.row < 6) and (2 < self.col < 6): return 4
    if (2 < self.row < 6) and (5 < self.col): return 5
    if (self.row > 5) and (self.col < 3): return 6
    if (self.row > 5) and (2 < self.col < 6): return 7
    if (self.row > 5) and (5 < self.col): return 8
	
  def reduceCellCandidatesByRow(self):
    for r in range(MAX):
      if r != self.row and len(Cell.matrix[r][self.col].value) == 1:
        self.value -= Cell.matrix[r][self.col].value
  
  def reduceCellCandidatesByCol(self):
    for c in range(MAX):
      if c != self.col and len(Cell.matrix[self.row][c].value) == 1:
        self.value -= Cell.matrix[self.row][c].value
		
  def reduceCellCandidatesByBlock(self):
    for r in range(MAX):
      for c in range(MAX):
        if (Cell.matrix[r][c].block == self.block) and (r != self.row or c != self.col) \
          and len(Cell.matrix[r][c].value) == 1:
            self.value -= Cell.matrix[r][c].value
  
  ### updateCellBasedOnCandidateValuesInItsRowColAndBlock
  def updateCell(self):
    rowCandidates = []
    colCandidates = []
    blkCandidates = []
	
    for c in range(MAX):
      if c != self.col:
        rowCandidates += Cell.matrix[self.row][c].value
	
    for r in range(MAX):
      if r != self.row:
        colCandidates += Cell.matrix[r][self.col].value
	
    for r in range(MAX):
      for c in range(MAX):
        if r != self.row or c != self.col:
          if Cell.matrix[r][c].block == self.block:
            blkCandidates += Cell.matrix[r][c].value
	
    for num in self.value:
      if (num not in rowCandidates) or (num not in colCandidates) or (num not in blkCandidates):
        self.value = {num,}

  def tryToReduceCandidateValuesInCell(self):
    oldValue = deepcopy(self.value)
	
    if len(self.value) == 1:
      return False
	
    self.reduceCellCandidatesByRow()
    self.reduceCellCandidatesByCol()
    self.reduceCellCandidatesByBlock()

    self.updateCell()
	
    return self.value != oldValue
  
### end of Cell
POSSIBLE_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def setUpCanvas(root):
  root.title("Sudoku! A Tk/Python Graphics Program by Ben Zhang")
  canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
  canvas.pack(expand = YES, fill = BOTH)
  return canvas

def displayTheSudokuBoard(matrix):
  canvas.delete('all')
  canvas.create_rectangle(0, 0, 1370, 710, fill = 'BLACK')
  
  canvas.create_rectangle(375, 170, 735, 560, width = 4, outline = 'RED', fill = 'BLUE')
  
  kolor = 'RED'
  
  ### Horizontal Lines
  for r in range(MAX-1):
    line = canvas.create_line(375, r * 42 + 175 +42, 395 + 340, r * 42 + 175 + 42, width = 2, fill = 'GREEN')
  
  ### Vertical Lines
  for c in range(MAX-1):
    line = canvas.create_line(c * 40 + 375 + 40, 170, c * 40 + 375 + 40, 560, width = 2, fill = 'GREEN')
  
  
  for r in range(MAX):
    for c in range(MAX): # coded by B.Z, code on github, please don't submit as your own, thanks.
      if len(matrix[r][c].value) != 1:
        ch = ' '
      else:
        ch = list(matrix[r][c].value)[0]
  
      colorBasedOnIfInitial = 'RED'
	  
      if matrix[r][c].wasInitial:
        colorBasedOnIfInitial = 'YELLOW'
	  
      canvas.create_text(c * 40 + 395, r * 42 + 200, text = ch, fill = colorBasedOnIfInitial, font = ('Helvetica', 20, 'bold'))
	  
def createTheSudokuBoard():
  V =  [[0, 0, 1, 0, 0, 9, 0, 0, 0,],
	[0, 0, 7, 8, 0, 6, 0, 4, 0,],
	[0, 0, 0, 0, 4, 3, 0, 0, 0,],
	[0, 4, 0, 1, 0, 0, 0, 6, 0,],
	[0, 7, 6, 0, 0, 0, 2, 5, 0,],
	[0, 1, 0, 0, 0, 2, 0, 3, 0,],
	[0, 0, 0, 2, 7, 0, 0, 0, 0,],
	[0, 5, 0, 3, 0, 1, 9, 0, 0,],
	[0, 0, 0, 6, 0, 0, 3, 0, 0,],
	]
  
  """V =  [[2, 4, 8, 3, 9, 5, 7, 1, 6,],
	[5, 7, 1, 6, 2, 8, 3, 4, 9,],
	[9, 3, 6, 7, 4, 1, 5, 8, 2,],
	[6, 8, 2, 5, 3, 9, 1, 7, 4,],
	[3, 5, 9, 1, 7, 4, 6, 2, 8,],
	[7, 1, 4, 8, 6, 2, 9, 5, 3,],
	[8, 6, 3, 4, 1, 7, 2, 9, 5,],
	[1, 9, 5, 2, 8, 6, 4, 3, 7,],
	[4, 2, 7, 9, 5, 3, 8, 6, 0,],
	]
  """
  
  V =  [[8, 0, 0, 0, 0, 0, 0, 0, 0,],
	[0, 0, 3, 6, 0, 0, 0, 0, 0,],
	[0, 7, 0, 0, 9, 0, 2, 0, 0,],
	[0, 5, 0, 0, 0, 7, 0, 0, 0,],
	[0, 0, 0, 0, 4, 5, 7, 0, 0,],
	[0, 0, 0, 1, 0, 0, 0, 3, 0,],
	[0, 0, 1, 0, 0, 0, 0, 6, 8,],
	[0, 0, 8, 5, 0, 0, 0, 1, 0,],
	[0, 9, 0, 0, 0, 0, 4, 0, 0,],
	]
  
  matrix = []
  
  for r in range(MAX):
    row = []
    for c in range(MAX):
      row.append(Cell(V[r][c], r, c, matrix))
    matrix.append(row)
  return matrix

def solutionIsCorrect(matrix):
  cols = getCols(matrix)
  rows = getRows(matrix)
  groups = getGroups(matrix)
  
  #print("Columns checked!", verifySets(cols))
  #print("Rows checked!", verifySets(rows))
  #print("Groupings checked!", verifySets(groups))
  
  return verifySets(cols) and verifySets(rows) and verifySets(groups) 

def getCols(matrix):
  columns = []
  for c in range(MAX):
    column = []
    for r in range(MAX):
      column.append( matrix[r][c] )
    columns.append(column)
  
  #print(columns)
  
  return columns

def getRows(matrix):
  rows = []
  for r in range(MAX):
    row = []
    for c in range(MAX):
      row.append( matrix[r][c] )
    rows.append(row)
  
  #print(rows)
    
  return rows

def getGroups(matrix):
  groups = [[], [], [], [], [], [], [], [], []]
  for r in range(MAX):
    for c in range(MAX):
      groups[matrix[r][c].block].append(matrix[r][c])
  #print(groups)
  
  return groups
    

def verifySets( grouping ):
  for aSet in grouping:
    unusedVals = deepcopy(POSSIBLE_VALUES)
    for cell in list(aSet):
      if len(list(cell.value)) != 1:
        #print("Cell not locked in:", cell)
        return False # coded by B.Z, code on github, please don't submit as your own, thanks.
      if list(cell.value)[0] not in unusedVals: 
        #print( list(cell.value)[0], "not in list", unusedVals)
        return False
      else:
        #print( "removed:", list(cell.value)[0], "from list that is now", unusedVals )
        unusedVals.remove(list(cell.value)[0])
    
    if len(list(unusedVals)) > 1:
      #print("Group", aSet,  "is missing at least one value:", unusedVals)
      return False
      #print(list(unusedVals))
      #print("Group", aSet,  "is missing at least 'no' value:", unusedVals)
    
  return True

def printVerification(matrix):
  if solutionIsCorrect(matrix):
    canvas.create_text(565, 600, text = "This Sudoku is correct.", fill = 'WHITE', font = ('Helvetica', 20, 'bold'))
  else:
    canvas.create_text(565, 600, text = "Wrong!", fill = 'Red', font = ('Helvetica', 70, 'bold'))

def makeAllPossibleSimpleChangesToMatrix(matrix):
  BREAK = False
  CONTINUE = True
  while CONTINUE:
    BREAK = False
    for r in range(MAX):
      for c in range(MAX):
        reduced = matrix[r][c].tryToReduceCandidateValuesInCell()
        if reduced:
          BREAK = True
          break # code from github, please do not submit as own work
      if BREAK:
        break
    if not BREAK:
      CONTINUE = False
  
  return matrix

def restoreValues(matrix, oldMatrix):
  for r in range(MAX):
    for c in range(MAX):
      matrix[r][c].value = deepcopy(oldMatrix[r][c].value)
  return matrix
  

def coordsOfEasiestCell(matrix):
  big = 10
  sml = 2
  bestRow = -1
  bestCol = -1
  for r in range(MAX):
    for c in range(MAX):
      length = len(matrix[r][c].value)
      if sml <= length < big:
        big = length
        bestRow = r
        bestCol = c
  return (bestRow, bestCol)

def solveTheSudoku(matrix):
  matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
  if solutionIsCorrect(matrix):
    #print("Matrix good!")
    return matrix
  oldMatrix = deepcopy(matrix)
  #print("Recursed!")
  for r in range(MAX):
    for c in range(MAX):
      if not matrix[r][c].value:
        return matrix #bad matrix
  
  row, col = coordsOfEasiestCell(matrix)
  
  for candidates in matrix[row][col].value:
    matrix[row][col].value = {candidates,}
    matrix = solveTheSudoku(matrix)
    if solutionIsCorrect(matrix): # coded by B.Z, code on github, please don't submit as your own, thanks.
      return matrix
    matrix = restoreValues(matrix, oldMatrix)
  
  """for r in range(MAX):
    for c in range(MAX):
      if len(list(matrix[r][c].value)) > 1:
        candidates = list(matrix[r][c].value)
        print(candidates)
        for num in candidates:
          print("Trying value", num, "at", r, ",", c)
          matrix[r][c].value = {num,}
          matrix = solveTheSudoku(matrix)
          if solutionIsCorrect(matrix):
            print("Got answer!")
            return matrix
          matrix = restoreValues(matrix, oldMatrix)
          print("Restored.")
  """
  return matrix

from tkinter import *
from time import clock, sleep
from copy import deepcopy

root = Tk()
canvas = setUpCanvas(root)
MAX = 9

def main():
  matrix = createTheSudokuBoard()
  matrix = solveTheSudoku(matrix)
  displayTheSudokuBoard(matrix)
  printVerification(matrix)
  printElapsedTime()
  root.mainloop()
  
def printElapsedTime():
  print('\n---Total run time =', round(clock() - startTime, 2), 'seconds.')
  
if __name__ == '__main__': startTime = clock(); main()
