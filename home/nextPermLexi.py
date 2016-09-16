#   Next Lexicographic Permutation
#   Ben Zhang
#   2/11/14

def inversions(word):
    # returns the number of inversions in a word
    return len([1 for i in range(1, len(word))
                for j in range(i)
                if word[i] < word[j]])

def parity(word):
    # returns parity value, one or zero, of word
    # based on the number of inversions
    return inversions(word) % 2

def maxInversions(word):
    # returns maximum number of possible inversions
    # in word, considering length of word
    total = 0
    for i in range(len(word)):
        total += i
    return total

def sortedPlaceValue(letter, word):
    # returns a number representing its place if the word is sorted alphabetically
    ordered = ''.join(sorted(word))
    return ordered.index(letter)

def normalizedPValue(word):
    # returns the number of inversions the word has, minus the P value of its first letter
    # used in determining the next permutation of lexicographic order
    inv = inversions(word)
    pval = sortedPlaceValue(word[0], word)
    return inv - pval

def nextPVal(word):
    # returns 1 + the P value of word's first letter
    return sortedPlaceValue(word[0], word) + 1

def swapNxtPVal(word):
    #  swaps first letter in word with the letter whose P value is one higher
    ordered = ''.join(sorted(word))
    nextPValLetter = ordered[nextPVal(word)]
    wordPlace = word.index(nextPValLetter)
    return swap(word, 0, wordPlace)

def swap(word, index1, index2):
    # returns string with items at index1 and index2 swapped
    wordlist = list(word)
    wordlist[index1], wordlist[index2] = wordlist[index2], wordlist[index1]
    return ''.join(wordlist)
    

def nextLexiPerm(word):
    # returns permutation after word, in lexicographic order.
    if len(word) < 2: return word
    if normalizedPValue(word) == maxInversions(word[1:]):
        if nextPVal(word) >= len(word): # reached end of permutations, cycle around back to the first
            return word[::-1]
        nxt = word[0] + nextLexiPerm(word[1:]) # this should cycle the sub-permutation back around
        nxt = swapNxtPVal(nxt)  # once the sub-perm is cycled, swapping out the first letter with the next highest
                                # gets us the correct next permutation
    else:
        nxt = word[0] + nextLexiPerm(word[1:])
    return nxt

import sys
word = 'ABCDE'
limit = 25
if len(sys.argv) > 1:
    word = sys.argv[1]
if len(sys.argv) > 2:
    limit = int(sys.argv[2])
    
print(nextLexiPerm('BACD'))
'''
nxtword = word
for i in range(1, limit):
    print(str(i) + "\tTH LEXI PERM IS: " + nxtword)
    nxtword = nextLexiPerm(nxtword)
'''

