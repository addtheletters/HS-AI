#   Permutations
#   Ben Zhang
#   2/11/14


def printPerms(perms):
    # Prints out pemutations in perms, followed by the total number of permutations
    for perm in perms:
        print(perm)
    print("Permutation count: " + str(len(perms)))


def nthPerm(word, n):
    # Returns nth permutation of word, in basic order
    if word == "": return ""
    pos = n % len(word)
    newN = int((n-pos) / len(word))
    newSegment = nthPerm( word[1:], newN )
    return newSegment[:pos] + word[0] + newSegment[pos:]


import sys
word = 'ABCD'
if len(sys.argv) > 1:
    word = sys.argv[1]

for i in range(0, 24):
    print(str(i) + "\tTH BASIC PERM IS: " + nthPerm(word, i))
