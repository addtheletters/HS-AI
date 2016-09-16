### Ben Zhang
### Period 2
### 12/19/13


def invalid(num):
  aFewKnownInvalids = [0,8, 9, 10, 13]
  if num > 127:
    return True
  if num in aFewKnownInvalids:
    return True
  return False
    
  
def printFrequencyTable(stng, sortingRule = 0):
  
  if stng == None:
    print('Error: Bad Input: Null value')
    return
  
  if type(stng) is not str:
    print('Error: Bad Input: Not a String')
    return
  
  if stng == '':
    print('Error: Bad Input: String is empty')
    return
  
  stngLength = len(stng)
  
  if stngLength > 1000:
    print('Warning: String length greater than 1000. Formatting may be affected.')
  
  print('----String Statistics----')
  print('The raw string: \n--------------\n' + stng + '\n--------------')
  print('String length:', stngLength)
  
  
  def countCharacters(toCount):
    counterDict = {}
    for char in toCount:
      if char in counterDict:
        counterDict[char] = counterDict[char] + 1
      else:
        counterDict[char] = 1
    return counterDict
    
  charCounter = countCharacters(stng)
  uniqueCharacterCount = len(charCounter)
  
  print('Unique characters:', uniqueCharacterCount)
  print('Average frequency:', stngLength / uniqueCharacterCount)
  
  print("Space-equivalent characters represented on the right by 'sp'")
  print("Nonprintable / Oddly printed characters represented on the right by 'np'")
  
  def simplifyOrderingRule(rule):
    if (rule == 'a') or (rule == 'A') or (rule == 1):
      return 1
    if (rule == 'f') or (rule == 'F') or (rule == 2):
      return 2
    return 0
    
  def orderCounterDict(counterDict, orderingRule):  
    if orderingRule == 1:
      #print('Ordering alphabetically.')
      return sorted(counterDict)
    if orderingRule == 2:
      #print('Ordering by frequency.')
      return sortByFrequency(counterDict)
    
    return counterDict.keys()
  
  def sortByFrequency(counterDict):
    from copy import deepcopy
    dictCopy = deepcopy(counterDict)
    
    def getAndRemoveMax(aDict):
      maxkey = None
      maxfrequency = 0
      for key in aDict:
        if aDict[key] > maxfrequency:
          maxkey = key
          maxfrequency = aDict[key]
      aDict[maxkey] = -1
      return maxkey
    
    sortedKeys = []
    while len(sortedKeys) < len(counterDict):
      sortedKeys.append(getAndRemoveMax(dictCopy))
    
    return sortedKeys
    
  sortedCounterList = orderCounterDict(charCounter, simplifyOrderingRule(sortingRule))
  
  print()
  
  print('---Character Frequency Table---')
  
  charNumber = 1
  
  for char in sortedCounterList:
    showable = char
    
    if char.isspace():
      showable = 'sp'
    if invalid(ord(char)):
      showable = 'np'
    
    ident = '<Uni ID:'+"%5s"%str(ord(char))+'>\t'
    print("%4s"%(str(charNumber))+'. \t', ident ," appeared ",charCounter[char]," time(s).", " Character '",showable ,"'", sep = '')
    charNumber += 1
    
    
  print('---End of Table---')
  
  print()
  
  print('Options:')
  print('Use no second arguement to print in order of occurence.')
  print('\tExample: printFrequencyTable(stng)')
  print('Use a second arguement of "A" or "a" or 1 to print in dictionary order.')
  print('\tExample: printFrequencyTable(stng, "a")')
  print('Use a second arguement of "F" or "f" or 2 to print in order of frequency.')
  print('\tExample: printFrequencyTable(stng, 2)')

st = 'A+' + ''.join([chr(n) + '+' for n in (0, 9, 10, 13)])
#st = 'JKAHGKHGJKHAkgjKqhgjkdh qekH'
printFrequencyTable(st, 'f')

"""
Sample output:

----String Statistics----
The raw string: 
--------------
A++	+
+
--------------
String length: 10
Unique characters: 6
Average frequency: 1.6666666666666667
Space-equivalent characters represented on the right by 'sp'
Nonprintable / Oddly printed characters represented on the right by 'np'

---Character Frequency Table---
   1. 	<Uni ID:   43>	 appeared 5 time(s). Character '+'
   2. 	<Uni ID:   65>	 appeared 1 time(s). Character 'A'
   3. 	<Uni ID:    0>	 appeared 1 time(s). Character 'np'
   4. 	<Uni ID:    9>	 appeared 1 time(s). Character 'np'
   5. 	<Uni ID:   10>	 appeared 1 time(s). Character 'np'
   6. 	<Uni ID:   13>	 appeared 1 time(s). Character 'np'
---End of Table---

Options:
Use no second arguement to print in order of occurence.
	Example: printFrequencyTable(stng)
Use a second arguement of "A" or "a" or 1 to print in dictionary order.
	Example: printFrequencyTable(stng, "a")
Use a second arguement of "F" or "f" or 2 to print in order of frequency.
	Example: printFrequencyTable(stng, 2)



"""
  
  