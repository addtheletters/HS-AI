### Lab Quiz 1
### Ben Zhang
### 10/8/13

print("+-----", '-' * 72, '-+', sep = '')
print('|   ANTIFREEZE TABLE for 22-Quart Radiator, by Ben Zhang (10/8/13)             |')
print('|   Initial concentration in left column. Desired concentration in top row.    |')
print('|   Drain the amount shown in the table, and replace with pure antifreeze.     |')
print("+-----", '-' * 72, '-+', sep = '')
print('|RESULT =   10%    20%    30%    40%    50%    60%    70%    80%    90%   100% |')
print("+-----", '-' * 72, '-+', sep = '')
for B in range(0, 100, 10):
  print(" %2i"%B, '% | ', sep = '', end = '' )
  print(' Numbers go here.')
  print("     +", '-' * 72, '-+', sep = '')
