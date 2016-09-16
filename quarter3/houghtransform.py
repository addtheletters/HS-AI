#       Hough Transform
#       Ben Zhang
#       3.11.14
#       Period 2

from tkinter    import *
from random     import *
from time       import clock
from sys        import setrecursionlimit
setrecursionlimit(7000)

class ImageFrame:
  def __init__(self, pixels):
    self.img = PhotoImage(width = WIDTH, height = HEIGHT)
    for row in range(HEIGHT):
      for col in range(WIDTH):
        num = pixels[row*WIDTH + col]
        if COLORFLAG == True:
          kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])
        else:
          kolor = '#%02x%02x%02x' % (num, num, num)
          if pixels[row*WIDTH + col] == INTERMED:
            kolor = '#%02x%02x%02x' % (255, 0, 0)
        self.img.put(kolor, (col, row))
    c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
    c.create_image(0, 0, image = self.img, anchor = NW)
    printElapsedTime('displayed image')

def printElapsedTime(msg = 'time'):
  length = 30
  msg = msg[:length]
  tab = '.'*(length - len(msg))
  print('--' + msg.upper() + tab + ' ', end = '')
  time = round(clock() - START, 1)
  print( '%2d'%int(time/60), ' min:', '%4.1f'%round(time%60, 1), \
    ' sec', sep = '')    

def displayImageWindow(image):
  global x
  x = ImageFrame(image)

# ------------------------------------------------Coordinate utility functions
def getCoords(index):
  return [index//WIDTH, index%WIDTH]

def getIndex( row, col ):
  ind = (row * WIDTH) + col
  return ind

def isValidPixel( index ):
  if index < 0 or index >= WIDTH * HEIGHT:
    return False
  return True

def isInvalidPixel( cordsx, cordsy ):
  if cordsx < 0 or cordsy < 0:
    return True
  if cordsx >= WIDTH or cordsy >= HEIGHT:
    return True
  return False

def isBorderPixel( index ):
  cords = getCoords(index)
  if cords[0] < 1 or cords[1] < 1:
    return True
  if cords[0] >= WIDTH-1 or cords[1] >= HEIGHT-1:
    return True
  return False

def frange(start, stop, step):
  i = start
  terminate = stop-(step/10)
  while i < terminate:
    yield i
    i += step
#--------------------------------------------------------------------

#-------------------------------------------------------------Edge detection
def getGaussianMaskIndicesAndScalars( index ):
  coords = getCoords(index)
  indices = []
  indices.append( [getIndex(coords[0] - 1    , coords[1] - 1), 1] )
  indices.append( [getIndex(coords[0]        , coords[1] - 1), 2] ) # to the left
  indices.append( [getIndex(coords[0] - 1    , coords[1]    ), 2] ) # to the top
  indices.append( [getIndex(coords[0] + 1    , coords[1]    ), 2] ) # to the bottom
  indices.append( [getIndex(coords[0]        , coords[1] + 1), 2] ) # to the right
  indices.append( [getIndex(coords[0] + 1    , coords[1] + 1), 1] )
  indices.append( [getIndex(coords[0] - 1    , coords[1] + 1), 1] )
  indices.append( [getIndex(coords[0] + 1    , coords[1] - 1), 1] )
  return indices

def getXSobelMaskIndicesAndScalars( index ):
  coords = getCoords(index)
  indices = []
  indices.append( [getIndex(coords[0] - 1    , coords[1] - 1), -1] )
  indices.append( [getIndex(coords[0]        , coords[1] - 1), -2] ) # to the left
  indices.append( [getIndex(coords[0] - 1    , coords[1]    ), 0] ) # to the top
  indices.append( [getIndex(coords[0] + 1    , coords[1]    ), 0] ) # to the bottom
  indices.append( [getIndex(coords[0]        , coords[1] + 1), 2] ) # to the right
  indices.append( [getIndex(coords[0] + 1    , coords[1] + 1), 1] )
  indices.append( [getIndex(coords[0] - 1    , coords[1] + 1), 1] )
  indices.append( [getIndex(coords[0] + 1    , coords[1] - 1), -1] )
  return indices

def getYSobelMaskIndicesAndScalars( index ):
  coords = getCoords(index)
  indices = []
  indices.append( [getIndex(coords[0] - 1    , coords[1] - 1), 1] )
  indices.append( [getIndex(coords[0]        , coords[1] - 1), 0] ) # to the left
  indices.append( [getIndex(coords[0] - 1    , coords[1]    ), 2] ) # to the top
  indices.append( [getIndex(coords[0] + 1    , coords[1]    ), -2] ) # to the bottom
  indices.append( [getIndex(coords[0]        , coords[1] + 1), 0] ) # to the right
  indices.append( [getIndex(coords[0] + 1    , coords[1] + 1), -1] )
  indices.append( [getIndex(coords[0] - 1    , coords[1] + 1), 1] )
  indices.append( [getIndex(coords[0] + 1    , coords[1] - 1), -1] )
  return indices

def getCannyStructureCellsForAngle( index, approxAngle ):
  coords = getCoords(index)
  indices = []
  if approxAngle == 0:
    indices.append( getIndex(coords[0]        , coords[1] - 1) )
    indices.append( getIndex(coords[0]        , coords[1] + 1) )
    return indices
  if approxAngle == 1:
    indices.append( getIndex(coords[0]  + 1   , coords[1] - 1) )
    indices.append( getIndex(coords[0]  - 1   , coords[1] + 1) )
    return indices
  if approxAngle == 2:
    indices.append( getIndex(coords[0] + 1    , coords[1]   ) )
    indices.append( getIndex(coords[0] - 1    , coords[1]   ) )
    return indices
  if approxAngle == 3:
    indices.append( getIndex(coords[0] - 1    , coords[1] - 1) )
    indices.append( getIndex(coords[0] + 1    , coords[1] + 1) )
  return indices

def getNSEW( index ):
  coords = getCoords(index)
  indices = []
  indices.append( getIndex(coords[0]        , coords[1] - 1) ) # to the left
  indices.append( getIndex(coords[0] - 1    , coords[1]    ) ) # to the top
  indices.append( getIndex(coords[0] + 1    , coords[1]    ) ) # to the bottom
  indices.append( getIndex(coords[0]        , coords[1] + 1) ) # to the right
  return indices

def gaussianSmooth( image ):
  # retuns an image
  # defaults grid to all -1s
  product = [0] * (WIDTH * HEIGHT)
  for index in range(WIDTH * HEIGHT):
    if not isBorderPixel(index):
      maskParts   = getGaussianMaskIndicesAndScalars( index )
      total = image[index] * 4
      for part in maskParts:
        total += part[1] * image[part[0]]
      product[index] = total / 16
  return product

def theta( Gx, Gy ):
  def closestInt( radians ):
    diffs = [   abs(radians),
                abs(radians - (pi / 4)),
                abs(radians - (pi / 2)), 
                abs(radians - (pi * 3 / 4)),
                abs(radians - pi)
             ]
    mindiff = min(diffs)
    ind = diffs.index(mindiff) # Code on github. Respect honor code. Do not submit as your own. 
    if ind == 4: 
      ind = 0
    return ind 
    
  T = atan2( Gy, Gx ) % pi
  return closestInt(T)

def sobelTransform( image ):
  product = [ [0, 0, 0, 0, 0] for elt in range(WIDTH * HEIGHT) ]
  for index in range(WIDTH * HEIGHT):
    if not isBorderPixel(index):
      xMaskParts = getXSobelMaskIndicesAndScalars( index )
      yMaskParts = getYSobelMaskIndicesAndScalars( index )
      Gx = 0
      Gy = 0
      for part in xMaskParts:
        Gx += part[1] * image[part[0]]
      for part in yMaskParts:
        Gy += part[1] * image[part[0]]
      product[index][0] = sqrt( Gx*Gx + Gy*Gy )
      product[index][1] = theta( Gx, Gy )
  return product

def cannyTransform( sobel ):
  sobel = findStructEdges( sobel )
  sobel = doubleThreshold( sobel )
  return sobel

def findStructEdges( sobel ):
  for index in range(WIDTH * HEIGHT):
    if not isBorderPixel(index):
      structChecks = getCannyStructureCellsForAngle( index, sobel[index][1] )
      if sobel[index][0] > sobel[structChecks[0]][0]\
         and sobel[index][0] > sobel[structChecks[0]][0]:
        sobel[index][2] = 1
  return sobel

def doubleThreshold( sobel ):
  for index in range(WIDTH*HEIGHT):
    if not isBorderPixel(index):
      if sobel[index][2] == 1:
        if sobel[index][0] > HIGH:
          #print("hello")
          sobel[index][4] = 1
          fixCellAt(sobel, index)        
  return sobel

def fixCellAt(M, index):
  if isBorderPixel(index):
    return
  if M[index][3] == 1:
    return
  M[index][3] = 1
  if M[index][2] == 1 and M[index][0] > LOW:
    M[index][4] = 1
    neighbors = getNSEW( index )
    for nei in neighbors:
      fixCellAt( M, nei )
  return
#------------------------------------------------------------------------End Edge Detection



def addNoise(image, noisepoints):
  for pointnum in range(noisepoints):
    image[randint(0, (WIDTH * HEIGHT) - 1)] = 255

#sets image values
def drawLine(image, m, b, intensity = 255, start = 0, stop = 512):
  lastY = None
  for x in range(start, stop):
    y = m * x + b
    if y < WIDTH:
      ind = getIndex(int(y), x)
      if isValidPixel(ind):
        image[ind] = intensity
      if not lastY == None:
        smallerY = min(lastY, y)
        for intermediateY in range( int( abs( lastY - y ) )):
          intermediateInd = getIndex( int( smallerY + intermediateY ) , x)
          if isValidPixel(intermediateInd):
            image[intermediateInd] = intensity
      lastY = y
      
# increments image values instead of setting them      
def addLine(image, m, b, intensity = 1, start = 0, stop = 512):
  lastY = None
  for x in range(start, stop):
    y = m * x + b # Code on github. Respect honor code. Do not submit as your own. 
    if y < WIDTH:
      ind = getIndex(int(y), x)
      if isValidPixel(ind):
        image[ind] = image[ind] + intensity
      if not lastY == None:
        smallerY = min(lastY, y)
        for intermediateY in range( int( abs( lastY - y ) )):
          intermediateInd = getIndex( int( smallerY + intermediateY ) , x)
          if isValidPixel(intermediateInd):
            image[intermediateInd] = image[intermediateInd] + intensity
      lastY = y

def drawCircle(image, radius, xCen, yCen, intensity = 255):
  for x in range( xCen - radius, xCen + radius ):
    for y in range(yCen - radius, yCen + radius):
      if isInvalidPixel( x, y ):
        continue
      dx = x - xCen
      dy = y - yCen
      if sqrt(dx * dx + dy * dy) <= radius:
        image[getIndex(x, y)] = intensity
      #check if valid pixel
      #check if in circle
  return


def houghTransform(image):
   
  imageDiagonal = sqrt(HEIGHT**2 + WIDTH**2)
  radiusRange   = int(imageDiagonal + HEIGHT) + 1
  angleRange    = int( pi * ANGLEPRECISION )
  # Code on github. Respect honor code. Do not submit as your own. 
  accumulator = [0 for elt in range( angleRange * radiusRange )]
  
  for y in range(HEIGHT):
    for x in range(WIDTH):
      if image[getIndex(y, x)] < 255:
        continue
      for p in frange( 0, pi, PHISTEP ):
        theta = p - (pi / 2)
        r = x * sin(p) - y * cos(p)
        thetaIndex    = int( (theta + pi / 2) * ANGLEPRECISION )
        rIndex        = int(r + HEIGHT)
        accumulator[ rIndex * angleRange + thetaIndex ] += 1
  return accumulator

def normalize( image, intensity = 255 ):
  m = max(image)
  printElapsedTime( 'normalizing' )
  return [ int( x * intensity / m) for x in image ]

def deHough(houghLst): # Code on github. Respect honor code. Do not submit as your own. 
  imageDiagonal = sqrt(HEIGHT**2 + WIDTH**2)
  radiusRange   = int(imageDiagonal + HEIGHT) + 1
  angleRange    = int( pi * ANGLEPRECISION )
  
  maxIndex      = houghLst.index( max( houghLst ) )
  rIndex        = maxIndex // angleRange
  thetaIndex    = maxIndex % angleRange
  
  newR     = rIndex - HEIGHT
  newTheta = (thetaIndex / ANGLEPRECISION) - (pi / 2)
  
  newM = -1 / tan(newTheta)
  newB = newR / sin(newTheta)
  
  return [newM, newB]
  
  
def houghCircle( canny ):
  xyr = [-999] * 3
  linesheet = [0] * (WIDTH * HEIGHT)
      
  #
  #-------abandoned :(
  #

  for elm in xyr:
    if elm < 0:
      print( "Circle detect: Element" )
      return None
  return xyr

WIDTH           = 512
HEIGHT          = 512
ANGLEPRECISION  = 100
PHISTEP         = 0.05
THRESHOLD       = 500
LOW             = 30
HIGH            = 50
SMOOTHS         = 3

INTERMED        = 150

COLORFLAG = False
root    = Tk()
START   = clock()

from math import tan, atan, atan2, sin, cos, pi, sqrt


def main():     
  print("Coded by Ben Zhang, TJHSST class of 2015. Please respect the honor code.")
  image = [0] * (WIDTH * HEIGHT)
  addNoise(image, 50)
  
  drawLine(image, -3, 300, 255)
  #drawLine(image, 4, 100, 200)
  drawCircle(image, 50, 300, 300)
  
  #-----------hough line
  accumulator = houghTransform(image)
  result = deHough(accumulator)
  drawLine(image, result[0], result[1], INTERMED)
  #-------------------
  
  
  #---------edge detection
  smoothed = image
  for rep in range( SMOOTHS ):
    smoothed = gaussianSmooth( smoothed )
    print("smoothed, number", str(rep + 1))
    
  sobeled = sobelTransform(smoothed)
  cannied = cannyTransform(sobeled)
  print("ok!")
  sth = normalize( [x[4] for x in cannied] )
  displayImageWindow( sth )
  #--------------
  
  displayImageWindow(image)
  root.mainloop()
  
  
def testDeHough(image):
  m = 3
  b = 300
  x = 30
  y = m * x + b
  
  assert y == m*x + b, ['error']
  
  phi = atan(m)
  theta = phi - (pi / 2)
  r = x * sin(phi) - y * cos(phi)
  
  imageDiagonal = sqrt(HEIGHT**2 + WIDTH**2)
  houghHeight   = int(imageDiagonal + HEIGHT) + 1
  houghWidth    = int( pi * 100 )
  houghLst = [0] * (houghHeight * houghWidth)
  
  print('len of houghLst is', len(houghLst))
  
  thetaIndex    = int( (theta + pi / 2) * 100 )
  rIndex        = int(r + HEIGHT)
  
  houghLst[ rIndex * houghWidth + thetaIndex ] += 1
  
  maxIndex = houghLst.index( max( houghLst ) )
  
  rIndex        = maxIndex // houghWidth
  thetaIndex    = maxIndex % houghWidth
  
  newR     = rIndex - HEIGHT
  newTheta = (thetaIndex / 100) - (pi / 2)
  
  newM = -1 / tan(newTheta)
  newB = newR / sin(newTheta)
  
  newY = newM * x + newB
  
  percentError = ((y - newY) / y) * 100
  
  print( 'x =', x, 'and y =', round(newY, 2), 'and yerror =', round(percentError, 2) )
  
  
  drawLine( image, m, b )
  drawLine( image, newM, newB)
  
if __name__ == '__main__':
  main()





