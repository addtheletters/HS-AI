#       Permutation Quiz
#       17 Feb 2013
#       Ben Zhang

def numPerms(size):
  total = 1
  for ind in range(2, size+1):
    total = ind * total
  return total

def permute(Lst, r):
  if len(Lst) < 2:
    return Lst
  subC = numPerms(len(Lst) - 1)
  cP = r // subC
  rem = r % subC
  manip = Lst[:]
  manip.remove(Lst[cP])
  return [Lst[cP]] + permute(manip, rem)

print(permute([0, 1, 2, 3], 13))

