### Ben Zhang
### Period 2
### 11/26/13

def minDotProd(x, y):
  a = x[:]
  b = y[:]
  total = 0
  while len(a) > 0:
    aMin = min(a)
    bMax = max(b)
    total = total + (bMax * aMin)
    a.remove(aMin)
    b.remove(bMax)
  return total

def minDotProd2(x, y):
  a = x[:]
  b = y[:]
  a.sort()
  b.sort()
  total = 0
  for index in range(len(a)):
    total = total + a[index] * b[len(b) - index - 1]
  return total

def minDotProd3(x, y):
  a = x[:]
  b = y[:]
  a.sort()
  sorted(b, reverse = True)
  total = 0
  for index in range(len(a)):
    total = total + a[index] * b[index]
  return total
  
def minDotProd4(x, y):
  a = x[:]
  b = y[:]
  a.sort()
  sorted(b, reverse = True)
  zipped = list(zip(a, b))
  return sum( [ aval*bval for aval, bval in zipped ]  )
  
def main():
  x = [3, 4, 5]
  y = [5, 6, 7]
  dotproduct = minDotProd(x, y)
  print(dotproduct)
  dotproduct2 = minDotProd2(x, y)
  print(dotproduct2)
  dotproduct3 = minDotProd3(x, y)
  print(dotproduct3)
  dotproduct4 = minDotProd4(x, y)
  print(dotproduct4)

if __name__ == '__main__': main()
