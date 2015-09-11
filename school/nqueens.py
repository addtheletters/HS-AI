#       Ben Zhang      
#       Period 2
#       2014-04-08

def printBoard( board ):
  size = len(board)
  error = [False, -1, -1]
  print( '#' * (size*2 + 3) )
  for loc in board:
    if loc >= size:
      error[0] = True
      error[1] = loc
      error[2] = board.index(loc)
    linestr = "# "
    for ind in range(size):
      if ind == loc:
        linestr += "Q "
      else:
        linestr += "- "
    linestr += "#"
    print(linestr)
  print( '#' * (size*2 + 3) )
  if error[0]:
    print('Faulty position in board: location:', error[1], ', index:', error[2])
  return error

def findFewestAttacks( perms, original ):
  best = original
  fewest = countAttacks(original)
  for perm in perms:
    attacks = countAttacks(perm)
    if attacks <= fewest:
      best = perm
      fewest = attacks
  return best

def hillclimb(board, depthlim = 10):
  oldbest = board
  fewest = countAttacks(board)
  depth = 0
  while True:
    depth += 1
    if depth > depthlim:
      break
    bestest = findFewestAttacks(get1PSwaps(oldbest), oldbest)
    attacks = countAttacks(bestest)
    if bestest == oldbest:
      break
    oldbest = bestest
    fewest = attacks
  ##print('no')
  return oldbest

def findSolution( N, maxtries = 30 ):
  bestmin = float('inf')
  tries = 0
  solution = []
  while bestmin > 0:
    tries += 1
    if tries > maxtries:
      print( 'Exceeded max tries.' )
      break
    ran         = getRandomBoard(N)
    localbest   = hillclimb(ran)
    localmin    = countAttacks(localbest)
    
    if localmin <= bestmin:
      bestmin   = localmin
      solution  = localbest
  return solution

def countAttacks( board ):
  #     only counts diagonal attacks!
  size  = len(board)
  count = 0
  for index in range(size):
    qplace = board[index]
    for row in range(size):
      dist = row - index
      if dist == 0: 
        continue
      if board[row] == qplace - dist or board[row] == qplace + dist:
        count += 1
  return count // 2 #should always be a whole number...

# if elements of board castable to ints, returns int-form of board
def getIntBoard( board ):
  reserve = [0] * len(board) 
  for ind in range(len(board)):
    reserve[ind] = int(board[ind])
  return reserve

# gets a random permutation
def getRandomBoard( size ):
  choices       = [ind for ind in range(size)]
  board         = []
  while len(choices) > 0:
    board.append( choices.pop( random.randrange(len(choices)) ) )
  return board

def swap( leest, index1, index2 ):
  leest[index1], leest[index2] = leest[index2], leest[index1]
  return leest
  
def get1PSwaps( original ):
  size = len(original)
  perms = []
  perms.append( original[:])
  for ind1 in range(size):
    for ind2 in range(ind1+1, size):
      aperm = original[:]
      perms.append(swap(aperm, ind1, ind2))
  return perms

def print1PSwaps( original ):
  size = len(original)
  print("One-swap permutations")
  print( original[:], "= parent")
  for ind1 in range(size):
    print('-' * (size*3))
    for ind2 in range(ind1+1, size):
      aperm = original[:]
      print(swap(aperm, ind1, ind2), "= group", ind1)
  
from time import clock
import sys, random
#board = getIntBoard(sys.argv[1:])
starttime = clock()
board = findSolution(40, 30)
printBoard( board )
print( "Attacks:", countAttacks( board ))
#print1PSwaps(board)
print( "Time spent is", round(clock()-starttime, 2), 'seconds.' )



