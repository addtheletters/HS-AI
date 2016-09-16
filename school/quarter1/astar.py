### A STAR
### Ben Zhang

"""
graph = {'A': [('Z', 75), ('T', 118), ('S', 140)],
            'Z': [('A', 75), ('O', 71)],
	    'T': [('A', 118), ('L', 111)],
	    'L': [('T', 111),('M', 70)],
	    'M': [('L', 70),('D', 75)],
	    'D': [('M', 75),('C', 120)],
	    'C': [('D', 120),('R', 146),('P', 138)],
	    'R': [('C', 146),('P', 97),('S', 80)],
	    'S': [('R', 80),('F', 99),('O', 151),('A', 140)],
	    'O': [('S', 151),('Z', 71)],
	    'P': [('C', 138),('R', 97),('B', 101)],
	    'F': [('S', 99),('B', 211)],
	    'B': [('P', 101),('F', 211),('G', 90),('U', 85)],
	    'G': [('B', 90)],
	    'U': [('B', 85),('H', 98),('V', 142)],
	    'H': [('U', 98),('E', 86)],
	    'E': [('H', 86)],
	    'V': [('U', 142),('I', 92)],
	    'I': [('V', 92),('N', 87)],
	    'N': [('I', 87)],
    }
    
"""


graph = {'A':[366,3,('Z',75),('T',118),('S',140)],
       'Z':[374,2,('A',75),('O',118)],
       'T':[329,2,('A',118),('L',111)],
       'L':[244,2,('T',111),('M',70)],
       'M':[241,2,('L',70),('D',75)],
       'D':[242,2,('M',75),('C',120)],
       'C':[160,3,('D',120),('R',146),('P',138)],
       'R':[193,3,('C',146),('P',97),('S',80)],
       'S':[253,4,('R',80),('F',99),('O',151),('A',140)],
       'O':[380,2,('S',151),('Z',71)],
       'P':[100,3,('C',138),('R',97),('B',101)],
       'F':[176,2,('S',99),('B',211)],
       'B':[0,4,('P',101),('F',211),('G',90),('U',85)],
       'G':[77,1,('B',90)],
       'U':[80,3,('B',85),('H',98),('V',142)],
       'H':[151,2,('U',68),('E',86)],
       'E':[161,1,('H',86)],
       'V':[199,2,('U',142),('I',92)],
       'I':[226,2,('V',92),('N',87)],
       'N':[234,1,('I',87)]}
 


def main():
  print("This code was written by Ben Zhang, TJHSST class of 2015. No cheating, please!")
  print(astar('A', 'B'))  
  
def astar(rootNode, goalNode):
  Q = [ (0 + 366 ,rootNode, [], 0) ]
  CLOSED = {}
  
  while Q:
    (fValue, node, path, gValue) = Q.pop(0)
    
    if node == goalNode:
      print(path)
      
    CLOSED[node] = gValue
    
    for (child, localDist) in graph[node][2:]:
      nodeTuple = (graph[child][0]+localDist, child, path + [node], localDist)
      if child in CLOSED: #This code was written by Ben Zhang, class of 2015. No cheating, please!
        if CLOSED[child] > localDist:
          del CLOSED[node]
          Q.append(nodeTuple) ##???
      
      found = False
      foundToople = None
      
      for toople in Q:
        if child == toople[1]:
          foundToople = toople
      
        if not found:
          Q.append(nodeTuple)
        else:
          if toople[3] > localDist:
            Q.remove(foundToople)
            Q.append(nodeTuple)

if __name__ == '__main__': main()
  