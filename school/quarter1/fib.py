### Fibonacci
### Ben Zhang
### Period 2


from sys import setrecursionlimit; setrecursionlimit(1100)
from time import clock; START = clock()
from math import sqrt

def main():
  ##te = int(input("num? "))
  
  ##print('1(70):', fib1(70))
  ##print('2(36):', fib2(36))
  ##print('3(100000):', fib3(100000))
  ##print('4(39):', fib4(39))
  ##print('5(12):', fib5(12))
  ##print('6(1050):', fib6(1200))
  print('7(70):', fib7(70))
  printElapsedTime()

def fib1(p):
  a, b = 1, 1
  for n in range(2, p):
    c = a
    a = a + b
    b = c
  return a

def fib2(p):
  if p == 1 or p == 2: return 1
  return fib2(p-1) + fib2(p-2)

def fib3(p):
  a, b = 1, 1
  for n in range(2, p):
    a, b = a+b, a
  return a

def fib4(p):
  if p == 1 or p == 2: return 1
  if p == 3: return 2
  if p == 5: return 3
  return fib2(p-1) + fib2(p-2)

def fib5(p):
  return {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55, 11:89, 12:144}[p]

def fib6(p, d = {1:1, 2:1}):
  if p in d:
    return d[p]
  d[p] = fib6(p-1, d) + fib6(p-2, d)
  return d[p]

def fib7(p):
  return round( (1/sqrt(5))*(((1+sqrt(5))/2)**p - ((1-sqrt(5))/2)**p) )




def printElapsedTime():
  print('\n---Total run time =', round(clock() - startTime, 2), 'seconds.')
  
if __name__ == '__main__': startTime = clock(); main()