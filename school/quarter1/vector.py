class Cost():
  def cost(self):
    from math import sin
    if(0 < self._data[0] < 10) and (0 < self._data[1] < 10):
      return (self._data[0] * sin(4*self._data[0]) + 1.1*self._data[1] * sin(2*self._data[1]))
    return float('inf')
  
  def sort(A,B,C):
    if B.cost() > C.cost(): B.swap(C)
    if A.cost() < B.cost(): A.swap(B)
    if A.cost() < C.cost(): A.swap(C)
    return [B, C, A]
  
  def sortList(vectorList):
    if type(vectorList) != list:
      exit('ERROR: The Cost.sort function is limited to a list of elements.')
    vectorList.sort(key = Vector.cost)
    return vectorList
  
  def minVec(self, V):
    if self.cost() < V.cost(): return self
    return V
  
class Vector(Cost):
  
  def __init__(self, *_data):
    if type(_data[0]) == Vector:
      self._data = list(_data[0])
      return
    if type(_data[0]) == list:
      self._data = _data[0]
      return
    if type(_data[0]) == tuple:
      self._data = list(_data[0])
      return
    self._data = list(_data)
    
  def __repr__(self):
    return repr(self._data)
  
  def print(self, n = 2):
    print("Vector <", end = "")
    for i in range(len(self._data)-1):
      print(round(self._data[i], n), sep = ', ', end = ", ")
    print(round(self._data[i+1], n), end = "")
    print("> ")
    return self
  
  def length(self):
    return (len(self._data))
  
  def scalars(self):
    return self._data
  
  def equals(self, other):
    self._data = other._data[:]
    return Vector(self._data)
  
  def dist(self, other):
    return (self - other).mag()
  
  def dotProd(self, other):
    return sum([self._data[i]*other._data[i] for i in range(len(self._data))])
  
  def crossProd(X, Y):
    return Vector(X._data[1] * Y._data[2] - X._data[2]* Y._data[1],
		  X._data[2] * Y._data[0] - X._data[0]* Y._data[2],
		  X._data[0] * Y._data[1] - X._data[1]* Y._data[0])
  def mag(self):
    from math import sqrt
    return sqrt(sum([i * i for i in self._data]))
  
  def normalize(self):
    m = self.mag()
    self._data = (self/m)._data
    return self
  
  def swap(A, B):
    T = Vector(A)
    A.equals(B)
    B.equals(T)
    
  def null(self):
    return Vector([0] * self.length())
  
  def matrixMult(self, M):
    if self.length() is not len(M):
      exit('Inner dimensions of vector and matrix not equal.')
    W = [0] * len(M[0])
    sum = 0
    for col in range(len(M[0])):
      for i in range(self.length()):
        sum += self._data[i] * M[i][col]
      W[col], sum = sum, 0
    return Vector(W)
  
  def __add__(self, other):
    return Vector(*[self._data[i] + other._data[i] for i in range(len(self._data))])
  
  def __sub__(self, other):
    #print(type(other))
    return -other + self
  
  def __mul__(self, entity):
    if isinstance(entity, (Vector)):
      return self.crossProd(entity)
    if isinstance(entity, (int, float)):
      return Vector(*[ i * entity for i in (self._data) ] )
    if isinstance(entity, (list)):
      return self.matrixMult(entity)
    return NotImplemented
  
  def __rmul__(self, entity):
    return self * entity
  
  def __truediv__(self, num):
    if num == 0:
      return NotImplemented
    return self * (1.0/num)
  
  def __eq__(self, other):
    return (self._data == other._data[:])
  
  def __ne__(self, other):
    return not(self._data == other._data)
  
  def __neg__(self):
    return Vector(*[-i for i in self._data])
  
  def __getitem__(self, index):
    return self._data[index]
  
  def __setitem__(self, index, num):
    self._data[index] = num
    return self
  
def main():
  A = Vector(1, 2, 3)
  B = Vector([4, 5, 6])
  C = Vector((7, 8, 9))
  
  print(' 1.', Vector.sortList([C,B,A]))
  print(' 2.', Vector.sort(A,B,C))
  print(' 3. Vector A = ', A)
  print(' 4. Vector B = ', B)
  print(' 5. Vector C = ', C)
  
  D = Vector(A)
  E = Vector(B)
  D.swap(E)
  
if __name__ == "__main__": main()