  #     2 layer neural network
  #     Ben Zhang
  #     Period 2

def calculateError( 
                    inputVector, # len3 list
                    tier1Weights = [],
                    tier2Weights = [],
                    tier3Weights = []
                   ):
  inputVector.append(-1)
  for weightMatr in [tier1Weights, tier2Weights, tier3Weights]:
    if weightMatr == []:
      weightMatr = randomMatrix( len(inputVector), 2 )
  
  sad = 3
  face = 2
  sadface = sad + face
  print( sadface )
  return 0
  
from random import random
from math import e

def sigmoid( x ):
  return 1 / ( 1 + pow(e, -x) )

def randomMatrix( rows, cols ):
  M = []
  for row in range(rows):
    darow = []
    for col in range(cols):
      darow.append( (random() * 0.8)+0.1 )
    M.append( darow )
  return M
  
def matrixMult( V, M ):
    if len(V) != len(M):
      print( "Bad dimensions:", V, M )
      return 'error'
    W = [0] * len(M[0])
    for wIndex in range( len(W) ):
      W[wIndex] = sum( [ (V[ind] * M[ind][wIndex]) for ind in range(len(M)) ] )
    return W
  
print("Code made available on Github. Please respect the honor code.")
print(calculateError([1, 0, 1]))
