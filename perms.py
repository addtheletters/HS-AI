#   Permutation Labs
#   Ben Zhang
#   2/5/14

def printPerms(perms):
    for perm in perms:
        print(str(normalizedPValue(perm)) + ", " + perm)
    print("Permutation count: " + str(len(perms)))

def filterUniquePerms(perms):
    # takes in list of perms
    # returns list of perms without duplicates
    aPerms = perms
    aPerms = [perm for i,perm in enumerate(perms)
              if aPerms.index(perm) == i]
    return aPerms

def sortWord(word):
    # returns word with letters sorted alphabetically
    return ''.join(sorted(word))


def basicPerms(word):
    # generates permutations for word in basic order
    # ABC, BAC, BCA, ACB, CAB, CBA
    if len(word) < 2: return [word]
    return [perm[:i] + word[0] + perm[i:]
            for perm in basicPerms(word[1:])
            for i in range(len(word))]


def lexiPerms(word):
    # generates permutations for word in lexicographic order
    # word must be passed to this pre-sorted alphabetically
    # ABC, ACB, BAC, BCA, CAB, CBA
    if len(word) < 2: return [word]
    return [word[i] + perm
            for i in range(len(word))
            for perm in lexiPerms(word[:i] + word[i+1:])]

def swapPerms(word):
    # generates permutations for word in swap order
    # meaning only adjacent swaps allowed
    # ABC, BAC, BCA, CBA, CAB, ACB
    if len(word) < 2: return [word]
    aPerms = []
    aSubPerms = swapPerms(word[1:])
    walkingLetter = word[0]
    walkFromLeft = True
    for perm in aSubPerms:
        if walkFromLeft:
            for i in range(len(word)):
                newWord = perm[:i] + walkingLetter + perm[i:]
                aPerms.append(newWord)
            walkFromLeft = False
        else:
            for i in range(len(word)):
                dex = len(word) - i - 1
                newWord = perm[:dex] + walkingLetter + perm[dex:]
                aPerms.append(newWord)
            walkFromLeft = True
    return aPerms

def uniquePerms(word):
    # returns unique permutations for word in lexicographic order
    # word should probably be passed pre-sorted alphabetically
    if len(word) < 2: return [word]
    aPerms = []
    for i in range(len(word)):
        aPerms += [word[i] + perm
                     for perm in uniquePerms(word[:i]+word[i+1:])
                     if word[i] + perm not in aPerms]
    return aPerms
    
def nthPerm(word, n):
    # returns nth permutation of word, out of basic order
    if word == "": return ""
    pos = n % len(word)
    newN = int((n-pos) / len(word))
    return  + word[:pos] + nthPerm(word[1:], newN)

def inversions(word):
    # returns the number of inversions in a word
    return len([1 for i in range(1, len(word))
                for j in range(i)
                if word[i] < word[j]])

def parity(word):
    return inversions(word) % 2

def maxInversions(word):
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
word = 'AABB'
if len(sys.argv) > 1:
    word = sys.argv[1]

perms = uniquePerms(word)
printPerms(perms)


nxtword = word
for i in range(1, 25):
    print(str(i) + "\tTH LEXI PERM IS: " + nxtword)
    #print(str(i) + "\tTH BASE PERM IS: " + nthPerm(word, i))
    nxtword = nextLexiPerm(nxtword)

