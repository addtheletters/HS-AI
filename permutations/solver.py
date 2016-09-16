#   "SEND MORE MONEY"
#   Alphametics solver using Permutations
#   Ben Zhang
#   2/17/14

from itertools  import *
from time       import *
from re         import *
from math       import *
import sys
import string


def solve(puzzle):
    uniqueChars = list(set(''.join(puzzle)))
    charCount = len(uniqueChars)
    if charCount > 10:
        print("Impossible puzzle. Too many unique characters ("
              + str(charCount) + ").")
        return
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    initialChars = list(set([word[0] for word in puzzle]))
    initialCharPerms = list(permutations( digits, len(initialChars)))
    nonInitialChars = list(set(uniqueChars).difference(set(initialChars)))
    digits.append('0')
    print("initial chars", initialChars)
    print("unique chars", uniqueChars)
    print("noninit chars", nonInitialChars)
    count = 0 # Code written by Ben Zhang, class of 2015. Please respect the honor code.
    for perm in initialCharPerms:
        subPerms = list(permutations(digits, len(nonInitialChars)))
        for subPerm in subPerms:
            table = getTable(initialChars, nonInitialChars, list(perm), list(subPerm))
            if checkMap(puzzle, table):
                count += 1
                print(''.join(puzzle).translate(table))
    print("Solution count:", count)
    return

def getTable(initialCharList, nonInitialCharList, initDigits, nonInitDigits):

    #totalCharList = initialCharList[:]
    #totalCharList.extend(nonInitialCharList)
    #totalChars = ''.join(totalCharList)

    totalChars = ''.join(initialCharList + nonInitialCharList)
    totalDigits = ''.join(initDigits + nonInitDigits)
    #print(initDigits)
    #print(nonInitDigits)

    #totalDigitList = initDigits
    #totalDigitList.extend(nonInitDigits)
    #totalDigits = ''.join(totalDigitList)
    
    #print(totalChars)
    #print(totalDigits)
    
    xlateTbl = str.maketrans(totalChars, totalDigits)
    return xlateTbl


def checkMap(aStr, xlateTbl):
    if '0' in ''.join(myStr[0] for myStr in aStr).translate(xlateTbl):
        return False
    mySum = sum(int(myStr.translate(xlateTbl)) for myStr in aStr[:-1])
    return mySum == int(aStr[-1].translate(xlateTbl))

print("Code written by Ben Zhang, class of 2015. Please respect the honor code.")
puzzle = "SEND MORE MONEY"
if len(sys.argv) > 3:
    puzzle = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3]
elif len(sys.argv) > 1:
    puzzle = sys.argv[1]
puzzle = findall('[A-Z]+', puzzle.upper()) # regex tokenizes into list of uppercase words

print("Puzzle: " + str(puzzle))
print("Solutions (if any):")
startTime   = clock()
solve(puzzle)
stopTime    = clock()
print("-------------------")
elapsedTime = stopTime - startTime
print("Time elapsed =", floor(elapsedTime / 60),
      "minute(s) and", round(elapsedTime % 60, 1), "second(s)")
