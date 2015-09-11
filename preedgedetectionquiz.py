#       Pre Edge-Detection Quiz
#       Ben Zhang
#       27 February 2014

from math import atan2, pi

def theta( Gx, Gy ):
  def closestInt( radians ):
    diffs = [   abs(radians),
                abs(radians - (pi / 4)),
                abs(radians - (pi / 2)), 
                abs(radians - (pi * 3 / 4)),
                abs(radians - pi)
             ]
    mindiff = min(diffs)
    ind = diffs.index(mindiff)
    if ind == 4: 
      ind = 0
    return ind 
    
  T = atan2( Gy, Gx ) % pi
  return closestInt(T)
  
  
print( theta( -10, 1 ) )

  
  
