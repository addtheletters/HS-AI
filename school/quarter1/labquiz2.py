### Lab Quiz 2
### Ben Zhang
### 10/17/13

print("+-----", '-' * 72, '-+', sep = '')
print('|   ANTIFREEZE TABLE for 22-Quart Radiator, by Ben Zhang (10/17/13)            |')
print('|   Initial concentration in left column. Desired concentration in top row.    |')
print('|   Drain the amount shown in the table, and replace with pure antifreeze.     |')
print("+-----", '-' * 72, '-+', sep = '')
print('|RESULT =   10%    20%    30%    40%    50%    60%    70%    80%    90%   100% |')
print("+-----", '-' * 72, '-+', sep = '')

A = 22.0

for B in range(0, 100, 10):
  print(" %2i"%B, '% | ', sep = '', end = '' )
  print('  ',end = '')
  for C in range(10, 110, 10):
    x = ( (A * ( (C-B)/100.0)) / ((-B/100) + 1.0) )
    if(x > 0):
      print( " %5.2f "%x, sep = '', end = '')
    else:
      print("       ",sep = '',end = '')
  print('|')
  print("     +", '-' * 72, '-+', sep = '')
