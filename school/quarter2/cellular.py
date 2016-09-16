### Ben Zhang
### Period 2
### 12/12/13

from tkinter import *

FONT_SIZE = 8
CHAR_HEIGHT = 11
GENERATIONS = 70

def setUpCanvas(root):
  root.title("Wolfram's cellular automata: A Tk/Python Graphics Program")
  canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
  canvas.pack(expand = YES, fill = BOTH)
  return canvas

def printList(rule):
  
  canvas.create_text(170, 20, text = 'Rule ' + str(rule), \
    fill = 'gold', font = ('Helvetica', 20, 'bold'))

  reversedRule = rule[::-1]
  
  L = [1, ]
  printPos = [650, 30]
  printstart = 650
  L = [0,0] + L + [0,0]

  for gen in range(GENERATIONS): # This code was written by Ben Zhang, TJHSST class of 2015. No cheating, please!
    for digit in L:
      if digit == 1:
        canvas.create_text(printPos[0], printPos[1], text = CHAR, fill = 'RED', font = ('Helvetica', FONT_SIZE, 'bold'))
      printPos[0] += FONT_SIZE
    printstart = printstart - FONT_SIZE
    printPos[0] = printstart
    printPos[1] += CHAR_HEIGHT

    NL = []
    for start in range(len(L) - 2):
      binNumber = L[start] + L[start+1] * 2 + L[start+2] * 4
      
      NL += [reversedRule[binNumber],]
    L = [0,0] + NL + [0,0]
    
  
root = Tk()
canvas = setUpCanvas(root)
#FSIZE = 8
CHAR = chr(9607)

def main():
  print("This code was written by Ben Zhang, TJHSST class of 2015. No cheating, please!")
  rule = [0, 0, 0, 1, 1, 1, 1, 0,]
  
  printList(rule)
  root.mainloop()
  
if __name__ == '__main__': main()

  
