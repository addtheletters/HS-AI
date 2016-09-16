# This file contains miscellaneous functions excerpted from the Othello program.

def computersMove(depth, player):
    depth = depth-1
    global M
    setOfMoveValuesAndMoves = []        # 1. WRITE THIS FUNCTION

    for r in range(8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        piecesTurnedOver = LocateTurnedPieces(r, c, player)
        if not piecesTurnedOver:
          continue
        makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player)
        setOfMoveValuesAndMoves.append((maxValue(depth, -player), r, c))
        takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player)
    
    minval, minr, minc = min(setOfMoveValuesAndMoves)
    
    return minr, minc, LocateTurnedPieces(minr, minc, player)
        
      
    # look at board
    # do moves x numPlys
    # if baseCase do baseCase thing
    
    # rest of boards don't need to be evaluated
    # just uses evaluations from base cases to determine worth
    
    # send up min and max until all plys are processed

#----------------------------------------------------------------------------------------------------Othello--

def maxValue(depth, player): # Return the MAXIMUM value of the boards created by appending black moves.
#---Initialize and check assertions.
    
    depth = depth - 1
    if depth == 0:
      return baseCaseForEvenPlyDepth(depth, player)
  
    global M
    assert player  == HUMAN
    setOfMoveValuesAndMoves = []
    
    for r in range(8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        piecesTurnedOver = LocateTurnedPieces(r, c, player)
        if not piecesTurnedOver:
          continue
        
        makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player)
        setOfMoveValuesAndMoves.append(minValue(depth, -player))
        takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player)
    
    if setOfMoveValuesAndMoves == []:
      return boardScore(player)
    
    maxval = max(setOfMoveValuesAndMoves)
    
    return maxval
    # look at all children
    # get the values of their worth from them
    # pick the highest
    # go up

#----------------------------------------------------------------------------------------------------Othello--
# Return the MINIMUM value of the boards created by appending white moves. Remember, the higher the value,
# the better for black.
def minValue(depth, player):
#---Initialize and check assertions.
    depth = depth - 1
    if depth == 0:
      return baseCaseForOddPlyDepth(depth, player)
    

    global M
    assert player == COMPUTER # = white
    setOfMoveValuesAndMoves = []        # 3. WRITE THIS FUNCTION
    
    for r in range(8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        piecesTurnedOver = LocateTurnedPieces(r, c, player)
        if not piecesTurnedOver:
          continue
        
        makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player)
        setOfMoveValuesAndMoves.append(maxValue(depth, -player))
        takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player)
    
    if setOfMoveValuesAndMoves == []:
      return boardScore(-player)
    
    minval = min(setOfMoveValuesAndMoves)
    return minval
    
#----------------------------------------------------------------------------------------------------Othello--



# Note that this function is identical to the maxValue function (and is called from the maxValue function),
# except that it does not get its points from its children. Instead, it uses an evaluation function. Why
# return the maximum? The higher the score the better for black.
def baseCaseForEvenPlyDepth(depth, player):
#---Initialize and check assertions.
    global M
    assert depth == 0, [depth]
    updateThePointMatrices()
    setOfMoveValuesAndMoves = []        # 2. WRITE THIS FUNCTION
    
    for r in range(8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        piecesTurnedOver = LocateTurnedPieces(r, c, player)
        if not piecesTurnedOver:
          continue
        
        makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player)
        setOfMoveValuesAndMoves.append(boardScore(player))
        takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player)
    
    if setOfMoveValuesAndMoves == []:
      return boardScore(player)
    
    maxval = max(setOfMoveValuesAndMoves)

    return maxval
    # evaluate all boards for worth to black
    # pick the highest one
    # go up
    
    # Hi Ellis when you eventually read this message I just wanted to say hi what up 
    
    
    
#----------------------------------------------------------------------------------------------------Othello--

#  This function is identical to the minValue function (and is called from the minValue function), except that
#  it does not get its points from its children. Instead, it uses an evaluation function.
def baseCaseForOddPlyDepth(depth, player):
    global M
    assert depth == 0, [depth]
    updateThePointMatrices()

    setOfMoveValuesAndMoves = []        # 3. WRITE THIS FUNCTION
    
    for r in range(8):
      for c in range(8):
        if M[r][c] != 0:
          continue
        piecesTurnedOver = LocateTurnedPieces(r, c, player)
        if not piecesTurnedOver:
          continue
        
        makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player)
        setOfMoveValuesAndMoves.append(boardScore(-player))
        takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player)
    
    if setOfMoveValuesAndMoves == []:
      return boardScore(-player)
      
    minval = min(setOfMoveValuesAndMoves)
    return minval
    
    
    # evaluate all boards for worth to black
    # pick the lowest one
    # do the lowest one
    # go up
    
    