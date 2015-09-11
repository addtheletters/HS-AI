###	Ben Zhang
###	9/12/13
###	Period 2


def main():
  for n in range (3):
    print ('num =', n)
  
  i = 0
  while i < 5:
    print ('i =', i)
    i += 1
  
  print()
  
  Q = []
  Q.append(1)
  Q.append(2)
  Q.append(3)
  Q.append(4)
  Q.append(5)
  print(Q)
  
  Q = Q[0:3] + [15689] + Q[3:5]
  print(Q)
  
  Q.insert(0, 7)
  print(Q)
  
  Q.append(256)
  print(Q)
  
  Q.pop(0)
  print(Q)
  
  Q.pop()
  print(Q)
  
  Q.remove(3)
  print(Q)
  
  minim = min(Q)
  print(Q)
  
  print()
  L = [3, 7, 1, 4, 10]
  for dex in range (0, 10):
    if dex not in L:
      print (dex, 'true')
    else:
      print (dex, 'false')
      
  
  
  from math import factorial, atan2, hypot, degrees, tan, pi
  print()
  print(hypot(5, 12))
  print(sum(L))
  print(round(1897.815697))
  print(max(L))
  print(factorial(20))
  print(bin(2921))
  print(atan2(9, 10))
  
  print()
  print(tan(pi / 4))
  
  print()
  li = [1,4,72,1,4]
  li2 = [elk*4 for elk in li]
  print(li)
  print(li2)
  
  print()
  from random import randint
  lis = [[randint(100,999) for col in range(5)] for row in range(3) ]
  print(lis)
  
  print()
  print(randint(1, 6))
  
  from random import random
  
  print()
  print(random() * 6 + 1)
  
  print()
  
  lees = [randint(10, 99) for index in range(10)]
  print(lees)
  lees.sort()
  print(lees)
  
  from random import shuffle
  
  shuffle(lees)
  print(lees)
  
  print(fibIt(5))
  print(fibRec(5))
  
  thingyin = int(input("Gimme nomnom "))
  print(thingyin + 1)
  
  print()
  
  kaldf = [1, 2, 105689]
  kald2 = [72, 136, 2749]
  
  print(kald2)
  print(kaldf)
  
  zipped = list(zip(kald2, kaldf))
  print(zipped)
  
  dotprod = [zipped[coord][0] * zipped[coord][1] for coord in range(3)]
  print(dotprod)
  
  print()
  
  toformat = 12.34
  print("%7.1f"%toformat)
  
  print("%5i"%123)
  
  print()
  
  stwing = 'abcdef'
  frag1 = stwing[:2]
  frag2 = stwing[3:]
  
  #s = stwing.replace('c', 'x')
  
  s = frag1 + 'x' + frag2
  
  print(stwing)
  print(s)
  r = stwing[::-1]
  print(r)
  
  characts = ['a', 'r', 'g', 'h']
  print(', '.join(characts))
  
  # Dictionaries
  
  print()
  
  diyoo = {'AAA':1, 'ADGH':156, 'MNA':716, 'NOITDOESNT':8196}
  print(diyoo)
  diyoo['WHY DOES THIS MAKE SO MUCH SENSE'] = 16
  
  del (diyoo['AAA'] )
  print(diyoo)
  
  print( diyoo['ADGH'] )
  
  graphX = {'A': [('Z', 75), ('T', 118), ('S', 140)],
	    'Z': [('A', 75), ('O', 71)],
	    'T': [('A', 118), ('L', 111)],
	    'L': [('T', 111),('M', 70)],
	    'M': [('L', 70),('D', 75)],
	    'D': [('M', 75),('C', 120)],
	    'C': [('D', 120),('R', 146),('P', 138)],
	    'R': [('C', 146),('P', 97),('S', 80)],
	    'S': [('R', 80),('F', 99),('O', 151),('A', 140)],
	    'O': [('S', 151),('Z', 71)],
	    'P': [('C', 138),('R', 97),('B', 101)],
	    'F': [('S', 99),('B', 211)],
	    'B': [('P', 101),('F', 211),('G', 90),('U', 85)],
	    'G': [('B', 90)],
	    'U': [('B', 85),('H', 98),('V', 142)],
	    'H': [('U', 98),('E', 86)],
	    'E': [('H', 86)],
	    'V': [('U', 142),('I', 92)],
	    'I': [('V', 92),('N', 87)],
	    'N': [('I', 87)],
    }
  
  #print(graphX)
  
  print()
  print( graphX['P'][0][1] )
  from math import sqrt
  ##print('Hi','Bye')
  print()
  
  ## Part 2
  
  print('Num','\t','Sq','\t','Sqrt','\t','Cubrt','\t','|','\t','Num','\t','Sq','\t' ,'Sqrt','\t','Cubrt')
  for numbra in range(0, 100):
    if numbra % 2 == 0:
      numbr = numbra + 1
      print( numbr, '\t', numbr**2,'\t', round(sqrt(numbr), 3),'\t',round(pow(numbr,1/3),3),'\t','|','\t', numbr+1, '\t', (numbr+1)**2,'\t',round(sqrt(numbr+1),3),'\t',round(pow(numbr+1,1/3), 3))
  
def fibIt(n):
  first = 1
  second = 1
  if n < 3:
    return 1
  else:
    for lala in range(2, n):
      #print('hi')
      first,second = second,(first+second)
    return second

def fibRec(n):
  if n < 3:
    return 1
  else:
    return fibRec(n-1) + fibRec(n-2)
  
  
    
if __name__ == '__main__': main()
