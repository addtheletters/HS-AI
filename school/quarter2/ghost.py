### Ben Zhang
### Period 2
### 11/21/13

from time import clock
from trie import Node
from random import randint

FILE = "ghostdict.java" # Why is it a .java file????

def main():
  root = getWords(FILE)
  printDirections()
  stng = ''
  ##print('Trie:')
  ##root.print('')
  ##print('End of Trie')

  #print(root.search('zodiac'))
  
  while True:
    stng = requestAndCheck('Human', root, stng)
    stng = requestAndCheck('Computer', root, stng)
    
  #print(stng)

  #word = spellWordFromString(root, "na")
  #print(word)

def printDirections():
  print("This code was written by Ben Zhang, TJHSST class of 2015. No cheating, please!")
  print("Welcome to GHOST!")
  print("Take a card, any card")
  print("and of course, enjoy your stay!")
  print("Just kidding. Enter your letters. Try to win.")

def getWords(filename):
  trie = Node("*")
  dictionary = open(filename)
  for word in dictionary:
    if len(word) >= 5:
      #print(word, len(word))
      trie.insert(word.lower().strip())
  dictionary.close()
  return trie

def isComputer(player):
  if player == 'Computer':
    return True
  return False

def requestAndCheck(player, root, stng):
  if not isComputer(player):
    stng += input(player + ', enter character! ').lower()[0]      # code provided
    print('Player has chosen. Word is now:', stng, '.', sep = '') # open source on
    if root.search(stng) == True:                                 # github; should not be submitted
      print("----------------------------------------------")     # as your own work.
      print(player, "loses because (s)he is bad. Also,", stng, "is a word.") # :)
      print("---The game is over. Awwwwwwwwwwwwwwwwwww. ---")
      exit()
    if root.fragmentInDictionary(stng) == False:
      print("----------------------------------------------")
      print(player, " loses because (s)he is bad. Also, '", stng, "'\n does not begin any word.", sep = '')
      print('[The computer\'s word was ', '"', spellWordFromString(root, stng[0:-1]), '".]', sep = '')
      print("---The game is over. D'awwwwwwwwwwwww...   ---")
      exit()
    return stng
  else:
    stng += chooseLetter(getDownDesignatedString(root, stng))
    print('Computer has chosen. Word is now:', stng, '.', sep = '')
    if root.search(stng) == True:
      print("----------------------------------------------")
      print(player, "loses because it spelled", stng, ".")
      print("---The game is over. Hm. I wonder why.     ---")
      exit()
    if root.fragmentInDictionary(stng) == False:
      print("----------------------------------------------")
      print(player, " loses because it is bad. Also, '", stng, "'\n does not begin any word. What?", sep = '')
      print("---The game is over. Wuhuhuhuhuhuh.        ---")
      exit()
    return stng

def getDownDesignatedString(root, stng):
  node = root
  stringcpy = stng
  #print('hi')
  while len(stringcpy) > 0:
    #print('stringcpy:',stringcpy,'>')
    #print('stng:',stng,'>')
    if node.children[stringcpy[0]].value == '$':
      print('Failed to travel down trie along path:', stng)
      return
    node = node.children[stringcpy[0]]
    #print('Node: ' +node.value + ' >')
    stringcpy = stringcpy[1:]
  
  return node

def chooseLetter(node):
  k = None
  for key in node.children:
    #print("key:",key,'>')
    if (k == None) or (randint(0, 3) == 0):
      if (key != '$'):
        k = key
  #print('letter chosen:', k)
  return k

def spellWordFromString(root, stng):

  word = stng[:]
  if root.fragmentInDictionary(stng):
    currentnode = getDownDesignatedString(root, stng)
    #print('currentnode:', currentnode.value, '>')
  else:
    return ("<ERROR: Unable to spell word from string", stng ,">")
  while word[-1] != '$':
    k = chooseLetter(currentnode)
    if k == None:
      word = word + currentnode.value
      break
    if k != '\n':
      word = word + currentnode.children[k].value
    currentnode = currentnode.children[k]

  #print('stng:',stng,'>')
  #print('word:',word,'>')
  return word[0:-1]
    
  #return ("<ERROR: Unable to spell word from string", stng ,">")


def printElapsedTime():
  print('\n---Total run time =', round(clock() - startTime, 2), 'seconds.')


  
if __name__ == '__main__': startTime = clock(); main()
