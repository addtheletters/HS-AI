### Ben Zhang
### 11/19/13
### Period 2

def repeatingDecimalToFraction(number, repLength):
  numerator = 1
  denominator = 1
  
  stringofnum = str(number)
  posofdec = stringofnum.index('.')
  integPart = stringofnum[:posofdec].replace('.', '')
  decPart = stringofnum[posofdec:].replace('.', '')
  
  
  if not isinstance(number, (int, float)):
    return 'number is not an int or float', ''
  if type(repLength) != int:
    return 'repLength is not an int', ''
  if repLength < 0:
    return 'repLength is less than 0', ''
  if type(number) == int:#special case 1
    return (numerator, denominator)
  if repLength > len(decPart):
    return 'repLength is greather than length of decimal portion', ''
  if repLength == 0: #special case 2
    numDecimalPlaces = len(decPart)
    multiplier = 10**numDecimalPlaces
    numerator = multiplier * number
    denominator = multiplier
    return (numerator, denominator)
  
  multiplier1 = 10**(len(decPart))
  multiplier2 = 10**(len(decPart)- repLength)
  numerator = 1+int(number * multiplier1 - number * multiplier2);
  denominator = multiplier1 - multiplier2
  return (numerator, denominator)

def fraction(intPart, decPart):
  if intPart < 0:
    print('Integer part less than zero')
    return 
  if decPart < 0:
    print('Decimal part less than zero')
    return
  
  stringDecimal = str(decPart)
  fac = int(10**len(stringDecimal))
  numerator = int( (intPart + decPart/fac) * fac - intPart  )
  denominator = fac - 1
  return numerator, denominator

def main():
  number, repLength = (2.11, 2)
  num, den = repeatingDecimalToFraction(number, repLength)
  if type(num) == type(''):
    print('Error encountered:', num)
  else:
    print('Answer:', (number, repLength), '=', str(num) + '/' + str(den) )

def oldmain():
  num, den = fraction(3, 141592)
  print('answer =', str(num) + '/' + str(den))

if __name__ == '__main__': main()  