#Ben Zhang
#Period 2

def computersMove(depth, player):
    print("This code was written by Ben Zhang, TJHSST class of 2015. No cheating, please!")
    depth = depth-1
    global M
    setOfMoveValuesAndMoves = []        # 1. WRITE THIS FUNCTION

    for r in range(8):
      for c in range(8):
        if M[r][c] == 0:
          continue
        piecesTurnedOver = LocateTurnedPieces(r, c, player)
        if piecesTurnedOver == 0:
          continue # please no turn in this is on github is cheating thanks
        makeTheMoveAndTurnOverThePieces(r, c, piecesTurnedOver, player)
        setOfMoveValuesAndMoves.append((maxValue(depth, -player), r, c, piecesTurnedOver))
        takeBackTheMoveAndTurnBackOverThePieces(r, c, piecesTurnedOver, player)
    
    minval = float( 'inf' )
    minitem = ()
    for item in setOfMoveValuesAndMoves:
      if item[0] < minval:
        minitem = item
        minval = item[0]
    
    return (minitem[1], minitem[2], minitem[3])
        
      