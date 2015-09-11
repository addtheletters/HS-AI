#       Ben Zhang      
#       Period 2
#       4/29/14

#       Simple Artificial Neural Network?

from random import random
import random

def train_ann( xarrs, alpha = 0.01, warr = [], acceptableError = 0.001, maxIterations = 3000 ):
  
  BOGUS = float('inf')
  
  minErrors = [BOGUS] * len(xarrs)
  
  if warr == []:
    warr = [3] * (len(xarrs[0]) - 1)
  
  while max(minErrors) > acceptableError:
    xarr = random.choice(xarrs)
    xindex = xarrs.index(xarr)
    
    #print("examining index", xindex)
    #print("inputs", xarr[:-1])
    
    t = xarr[len(xarr) - 1]
    error = t - f(dotprod( xarr[:-1], warr ))
    
    if minErrors[ xindex ] == BOGUS:
      minErrors[ xindex ] = abs(error)
    elif minErrors[xindex] >= abs(error):
      minErrors[ xindex ] = abs(error)
    
    count = 1
    while abs(error) > acceptableError and count < maxIterations:
      count += 1
      for ind in range(len(warr)):
        warr[ind] = warr[ind] + alpha * error * xarr[ind]
        
      y = f(dotprod( xarr[:-1], warr ))
      error = t - y
      
    #  print("xarr:", xarr)
    #  print("weights:", warr)
    #  print("count:", count, "error:", error)
    
    #if abs(error) <= acceptableError:
    #  print( "inner: acceptable error" )
    #if count > maxIterations:
    #  print( "inner: exceeeded max iterations" )
    for xind in range(len(minErrors)):
      tempxarr = xarrs[xind]
      temptarg = tempxarr[len(tempxarr)-1]
      minErrors[xind] = abs(calcError(temptarg, tempxarr[:-1], warr))

    
    #if minErrors[xindex] >= abs(error):
     # minErrors[ xindex ] = abs(error)
   # print("current min errors:", minErrors)

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

from math import exp

def f(dp):
    return round( 1/(1+exp( -dp)) )

def act( fret ):
    return int(round(fret, 1))

def ANN( warr, x1, x2 ):
  xarr = [-1, x1, x2]
  return act(f(dotprod( xarr, warr )))
  
  
xarrays = [[-1, 1, 1, 1],
         [-1, 1, 0, 1],
         [-1, 0, 1, 1],
         [-1, 0, 0, 0],]


weights = train_ann( xarrays, 0.01, [1, 1, 1]   )

print( ANN(weights, 1, 1) )

print( ANN(weights, 1, 0) )

print( ANN(weights, 0, 1) )

print( ANN(weights, 0, 0) )
