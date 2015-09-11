#       Ben Zhang   
#       Period 2
#       3.11.2014
#       Edge Detection / Masks Quiz

ROW = 3
COL = 3
  
def printImage( image ):
  for r in range(ROW):
    for c in range(COL):
      index = getIndex(r, c)
      print('%3d'%image[index], end = '') 
    print()
      
def getCoords(index):
  return [index//COL, index%COL]

def getIndex( row, col ):
  ind = (row * COL) + col
  if ind < 0:
    print("error: index is negative:",ind, row, col)
  return ind

def isBorderPixel( index ):
  cords = getCoords(index)
  if cords[0] < 1 or cords[1] < 1:
    return True
  if cords[0] >= ROW-1 or cords[1] >= COL-1:
    return True
  return False

def getMaskIndicesAndScalars( index ):
  coords = getCoords(index)
  indices = []
  indices.append( [getIndex(coords[0] - 1    , coords[1] - 1), 0] )
  indices.append( [getIndex(coords[0]        , coords[1] - 1), 0] ) # to the left
  indices.append( [getIndex(coords[0] - 1    , coords[1]    ), 1] ) # to the top
  indices.append( [getIndex(coords[0] + 1    , coords[1]    ), 0] ) # to the bottom
  indices.append( [getIndex(coords[0]        , coords[1] + 1), 1] ) # to the right
  indices.append( [getIndex(coords[0] + 1    , coords[1] + 1), 0] )
  indices.append( [getIndex(coords[0] - 1    , coords[1] + 1), 0] )
  indices.append( [getIndex(coords[0] + 1    , coords[1] - 1), 0] )
  return indices

image = []
for num in range(ROW * COL):
  image.append(num)

printImage(image)
print()

newImage = [0] * (ROW * COL)

for index in range(ROW * COL):
  if not isBorderPixel(index):
    maskIndicesAndScalars = getMaskIndicesAndScalars( index )
    for item in maskIndicesAndScalars:
      newImage[index] += image[item[0]] * item[1]

printImage(newImage)
    


