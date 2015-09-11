###	Ben Zhang
###	Quiz 1 Corrections (Loops)
###	9/12/13
###	Period 2

#-- 3
# n in range(1, 3, 1) returns a boolean value rather than running through the range.

#-- 7
# n+=1 in the loop doesn't affect the progress of n in the range, where I thought it did.

#-- 8
# I saw the if n == 4: break and thought that it would not print the 4, but the print statement came before it.

#-- 9
for n in range(1, 10):
    if n%2 == 0: continue
    print(n, end = "")
# I did not know what continue does, which is apparently to skip to the next iteration of the loop.

print()

#--10
t = 0
for n in range(1, 10, 2):
  n += 1
  t += 1
print("Total t = ", t)
# Similar to 7, I thought altering n in the loop would affect the progress through the range.

print()