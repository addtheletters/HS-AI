### Routes Lab
### Ben Zhang
### Period 2

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

def DFS_AnyPath(node, goalNode, path = [], closedSet = set()):
  
  closedSet.add(node)
  path = path + [node]
  
  if node == goalNode:
    return path
  
  for (child, dist) in graph[node]:
    
    if child not in closedSet:
      temppath = []
      temppath = DFS_AnyPath(child, goalNode, path, closedSet)
      if temppath != None:
        return temppath
      
  return None


def DFS_FewestNodes(node, goalNode, path = [], best = []):
  path = path + [node]
  
  if node == goalNode:
    return path
  
  for (child, dist) in graph[node]:
    temppath = []
    if (child not in path) or (len(best) > len(path)):
      temppath = DFS_FewestNodes(child, goalNode, path, best)
      if temppath != []:
        if len(temppath) < len(best):
          best = temppath[:]
      if best == []:
        best = temppath[:]
  return best


def DFS_LeastCost(node, goalNode, path = [], best = [], bestcost = 0):
  path = path + [node]
  if node == goalNode:
    return path, bestcost
  
  for (child, dist) in graph[node]:
    temppath = []
    if (child not in path):
      temppath, tempbestcost = DFS_LeastCost(child, goalNode, path, best, dist + bestcost)
      if temppath != []:
        if tempbestcost < bestcost:
          best = temppath[:]
          bestcost = tempbestcost
      if best == []:
        best = temppath[:]
        bestcost = tempbestcost
  return best, bestcost


def BFS_AnyPath(start, goalNode):
  Q = [start]
  ##return BFS_AnyPathRecurse(Q, goal)
  closedSet = set()
  while len(Q) > 0:
    node = Q.pop(0)
    closedSet.add(node)
    if(node == goalNode):
      return path
    for(child, dist) in graph[node]:
      if child not in closedSet:
        Q.append(child)
        
    

def BFS_AnyPathRecurse(Q, goalNode, path = [], closedSet = set()):
  
  node = Q.pop(0)
  path = path + [node]
  closedSet.add(node)
  
  if(node == goalNode):
      return path
  
  for(child, dist) in graph[node]:
    if(child == goalNode):
      return path + [child]
    
    if child not in closedSet:
      Q.append(child)
    
  
  return BFS_AnyPathRecurse(Q, goalNode, path, closedSet)

def BFS_LeastCost():
  
  
  return




def main():
  print("===DFS===")
  
  print("Some path:", DFS_AnyPath('A', 'B'))
  print("Bestest Path:", DFS_FewestNodes('A', 'B'))
  print("Least Cost Path:", DFS_LeastCost('A', 'B')[0])
  
  print("===BFS===")
  
  print("Some path:", BFS_AnyPath('A', 'B'))
  
  
if __name__ == '__main__': main()
