class Node(object):
  def __init__(self, value):
    self.value = value
    self.children = {}
    
  def __repr__(self):
    self.print()
    return ''
  
  def print(self, stng):
    for key in self.children:
      if key == '$':
        print(stng)
      else:
        self.children[key].print(stng+key)
        
  
  def display(self):
    if self.value == '$':
      return
    print('---Node---')
    print('self.value is', self.value)
    print('self.children: [', end = '')
    
    for key in self.children:
      if key != '$':
        print(key, sep = '', end = ', ')
    print(']')
    print('----------')
    
    for char in self.children:
      (self.children[char]).display()
      
  def insert(self, stng):
    if len(stng) == 0:
      self.children['$'] = Node('$')
    else:
      if (stng[0] not in self.children):
        self.children[stng[0]] = Node(stng[0])
      self.children[stng[0]].insert(stng[1:])
  
  def search(self, stng):
    #print('searching for', stng)
    
    if len(stng) == 0:
      for key in self.children:
        if key == '$':
          return True
    else:
      for key in self.children:
        if key == stng[0]:
          if self.children[key].search(stng[1:]):
            return True
            
    return False
  
  def fragmentInDictionary(self, stng):
    if len(stng) == 0:
      return True
    #print(stng)
    for key in self.children:
      if key == stng[0]:
        #print(key + ' is ' + stng[0])
        if self.children[stng[0]].fragmentInDictionary(stng[1:]):
          return True
    return False
  
  
from sys import setrecursionlimit; setrecursionlimit(1000)
from time import clock

def main():
  root = Node('*')
  root.insert('cat')
  root.insert('catnip')
  root.insert('cats')
  root.insert("can't")
  root.insert('dog')
  root.insert('dognip')
  root.insert('dogs')
  
  root.display()
  root.print('')
  
  print('SEARCH:', root.search('do'))
  print('SEARCH:', root.search('dogs'))
  print('SEARCH:', root.search('doga'))
  print('SEARCH:', root.search('dognip'))
  
  
  printElapsedTime()

def printElapsedTime():
  print('\n---Total run time =', round(clock() - startTime, 2), 'seconds.')
  
  
if __name__ == '__main__': startTime = clock(); main()
