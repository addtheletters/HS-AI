### Ben Zhang
### Period 2
### 12/17/13


def invalid(num):
  if num > 127:
    return True
  return False
    
  
def showString(stng):
  stngLength = len(stng)
  print("Unprintable characters represented by 'np'")
  
  print("Number of characters:",stngLength)
  
  charCounter = {}
  
  for char in stng:
    if char in charCounter:
      charCounter[char] = charCounter[char] + 1
    else:
      charCounter[char] = 1
  
  for char in charCounter:
    showable = char
    if char.isspace():
      showable = 'np'
    ident = '<Uni hex ID:'+"%3s"%hex(ord(char))[2:]+'>'
    print("Character '",showable,"' \t", ident ," shown \t",charCounter[char]," time(s).", sep = '')
    
    
st = 'A+' + ''.join([chr(n) + '+' for n in (0, 9, 10, 13)])

showString(st)

"""
Sample output:

Unprintable characters represented by 'np'
Number of characters: 10
Character 'A' 	<Uni hex ID: 41> shown 	1 time(s).
Character '' 	<Uni hex ID:  0> shown 	1 time(s).
Character 'np' 	<Uni hex ID:  9> shown 	1 time(s).
Character '+' 	<Uni hex ID: 2b> shown 	5 time(s).
Character 'np' 	<Uni hex ID:  a> shown 	1 time(s).
Character 'np' 	<Uni hex ID:  d> shown 	1 time(s).



"""
  
  