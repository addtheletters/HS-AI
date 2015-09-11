#       Machine Vision
#       Ben Zhang       
#       Period 2
#       2/20/14

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
        self.img.put(kolor, (col, row))
    c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
    c.create_image(0, 0, image = self.img, anchor = NW)
    printElapsedTime('displayed image')
    
def displayImageWindow(image):
  global x
  x = ImageFrame(image)
    
def confirmP3fileType(file1):
  stng = file1.readline().strip()
  if stng[0] + stng[1] != 'P3':
    print("ERROR: Filetype not P3.")
    print("Error info: First line of file is ->", stng)
    file1.close()
    exit()

def printElapsedTime(msg = 'time'):
  length = 30
  msg = msg[:length]
  tab = '.'*(length - len(msg))
  print('--' + msg.upper() + tab + ' ', end = '')
  time = round(clock() - START, 1)
  print( '%2d'%int(time/60), ' min:', '%4.1f'%round(time%60, 1), \
    ' sec', sep = '')
  
def readFileNumbersIntoString(file1):
  nums = file1.read().split()
  file1.close()
  if len(nums)%3 != 0:
    print('WARNING: Non-multiple-of-three numbers in file.')
    print('continuing anyways...')
    #exit()
  return nums

def convertStringRGBsToGrayInts(nums):
  img = []
  for pos in range(0, len(nums), 3):
    RGB = (int(nums[pos+0]), int(nums[pos+1]), int(nums[pos+2]))
    img.append( int(0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]) )
  return img
  
def printTitleAndSizeOfImageInPixels(image):
  print('INFO:')
  if len(image) != WIDTH * HEIGHT:
    print('ERROR: Stated filesize not equal to number of pixels')
    print('file length:', len(image))
    print('width:', WIDTH, 'height:', HEIGHT)
    exit()
  print('Number of pixels:', len(image))
  printElapsedTime('image extracted from file')
  
def readPixelColorsFromImageFile(IMAGE_FILE_NAME):
  imageFile = open(IMAGE_FILE_NAME, 'r')
  confirmP3fileType(imageFile)
  nums = readFileNumbersIntoString(imageFile)
  image = convertStringRGBsToGrayInts(nums)
  return image

#       Mask utility
def getCoords(index):
  return [index//WIDTH, index%WIDTH]
  
def getIndex( xcoord, ycoord ):
  ind = (xcoord * WIDTH) + ycoord
  if ind < 0:
    print("error: index is negative:",ind, xcoord, ycoord)
  return ind

def isBorderPixel( index ):
  cords = getCoords(index)
  if cords[0] < 1 or cords[1] < 1:
    return True
  if cords[0] >= WIDTH-1 or cords[1] >= HEIGHT-1:
    return True
  return False

def isValidPixel( index ):
  if index < 0 or index >= WIDTH * HEIGHT:
    return False
  return True
  
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

#       SMOOTHING! 
def gaussianSmooth( image ):
  # retuns an image
  # defaults grid to all -1s
  #print(len(image))
  product = [0] * (WIDTH * HEIGHT)
  for index in range(WIDTH * HEIGHT):
    if not isBorderPixel(index):
      maskParts   = getGaussianMaskIndicesAndScalars( index )
      total = image[index] * 4
      for part in maskParts:
        #if part[0] < 0:
        #print(image[part[0]], part[1])
        total += part[1] * image[part[0]]
        #print(total)
      product[index] = total / 16
  return product

def normalize( image, intensity = 255 ):
  m = max(image)
  printElapsedTime( 'normalizing' )
  return [ int( x * intensity / m) for x in image ]

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
  #print("hi")
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
  
  
from tkinter    import *
from time       import clock
from sys        import setrecursionlimit
from math       import atan2, pi, sqrt

setrecursionlimit(10000)

root    = Tk()
START   = clock()
WIDTH   = 512
HEIGHT  = 512
SMOOTHS = 6
LOW = 30
HIGH = 50
COLORFLAG = False

def main():
  #print('Starting!')
  imageFileName = 'lena.ppm'
  nums = list(readPixelColorsFromImageFile(imageFileName))
  #displayImageWindow( nums )
  
  smoothed = nums
  for rep in range( SMOOTHS ):
    smoothed = gaussianSmooth( smoothed )
    print("smoothed, number", str(rep + 1))

  sobeled = sobelTransform(smoothed)
  cannied = cannyTransform(sobeled)
  print("ok!")
  sth = normalize( [x[4] for x in cannied] )
  displayImageWindow( sth )
  root.mainloop()
  
if __name__ == '__main__': main()

