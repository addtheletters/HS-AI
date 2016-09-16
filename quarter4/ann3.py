#       Ben Zhang      
#       Period 2
#       5/15/14

#   ANN3?

import random
def train_ann( xarrs, alpha = 0.01, warr = [], acceptableError = 0.01, maxIterations = 3000 ):
  
  BOGUS = float('inf')
  
  minErrors = [BOGUS] * len(xarrs)
  # Code written by Ben Zhang, class of 2015. Please respect the honor code.
  if warr == []:
    warr = [3] * (len(xarrs[0]) - 1)
  
  while max(minErrors) > acceptableError:
    xarr = random.choice(xarrs)
    xindex = xarrs.index(xarr)
    
    t = xarr[len(xarr) - 1]

    #print("examining index", xindex)
    #print("inputs", xarr[:-1])
    #print("target", xarr[len(xarr)-1])
    
    error = t - f(dotprod( xarr[:-1], warr ))
    
    if minErrors[ xindex ] == BOGUS:
      minErrors[ xindex ] = abs(error)
    elif minErrors[xindex] >= abs(error):
      minErrors[xindex] = abs(error)
    
    count = 1
    while abs(error) > acceptableError and count < maxIterations:
      count += 1
      for ind in range(len(warr)):
        warr[ind] = warr[ind] + alpha * error * xarr[ind]
        
      y = f(dotprod( xarr[:-1], warr ))
      error = t - y
      
      #print("xarr:", xarr)
      #print("weights:", warr)
      #print("count:", count, "error:", error)
    
    #if abs(error) <= acceptableError:
    #  print( "inner: acceptable error" )
    #if count > maxIterations:
    #  print( "inner: exceeeded max iterations" )
        
    for xind in range(len(minErrors)):
      tempxarr = xarrs[xind]
      temptarg = tempxarr[len(tempxarr)-1]
      minErrors[xind] = abs(calcError(temptarg, tempxarr[:-1], warr))


  return warr

def calcError(target, ins, weights):
    y = f(dotprod( ins, weights ))
    error = target - y
    return error
    
def dotprod( xarr, warr ):
  val = 0
  for ind in range(len(xarr)):
    val += xarr[ind] * warr[ind]
  return val

def f_old(val):
  if val > 0:
    return 1
  return 0

from math import e

def f(val):
    return 1/(1+pow(e, -val))

def act( fret ):
    return int(round(fret, 1))

def ANN( warr, x1, x2, x3 ):
  xarr = [-1, x1, x2, x3]
  return act(f(dotprod( xarr, warr )))

def getRand( lenn ):
  return [ (random.random() * 2 - 1) for ind in range(lenn) ]
  
xarrays = [[-1, 1, 1, 0, 0],
         [-1, 1, 0,   0, 1],
         [-1, 0, 1,   0, 1],
         [-1, 0, 0,   1, 0],]

print("Code made available on Github. Please respect the honor code.")
weights = train_ann( xarrays, 0.01, getRand(4)   )

print( ANN(weights, 1, 1, 0) )

print( ANN(weights, 1, 0, 0) )

print( ANN(weights, 0, 1, 0) )

print( ANN(weights, 0, 0, 1) )
