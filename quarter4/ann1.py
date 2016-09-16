#       Ben Zhang      
#       Period 2
#       4/29/14

#       Simple Artificial Neural Network?

from random import random

def train_ann(x0 = 2, x1 = 6, w0 = random() * 2 - 1, w1 = random() * 2 - 1, t = 0, alpha = 0.01, acceptableError = 0.0000001, maxIterations = 3000):
  error = t - ann_eval(w0, w1, x0, x1)
  count = 1
  
  while abs(error) > acceptableError and count < maxIterations:
    count += 1
    w0 = w0 + alpha * error * x0
    w1 = w1 + alpha * error * x1
    y = ann_eval(w0, w1, x0, x1)
    error = t - y
    print("count:", count, "error:", error)
    
  if abs(error) < acceptableError:
    print( "acceptable error" )
    
  if count > maxIterations:
    print( "exceeeded max iterations" )
  
  return w0, w1


def ann_eval( w0, w1, x0, x1 ):
  y = w0*x0 + w1*x1
  return y

def f(y, threshold = 0.01):
  if abs(y) < threshold:
    return True
  return False

def ANN(w0, w1, x0, x1):
  return f(ann_eval(w0, w1, x0, x1))

w0, w1 = train_ann(2, 6, 1000, 1000)
print(w0, w1)
print( ANN( w0, w1, 2, 6 ) )
print( ANN( w0, w1, 1000, 3000 ) )
print( ANN( w0, w1, 40000, 120000) )
print( ANN( w0, w1, 40000, 120000 + 1) )

