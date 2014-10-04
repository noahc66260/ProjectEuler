# The program runs in 1-2 minutes so even though I have an answer I just
# want to share my thoughts for a faster implementation.
# Have two arrays of size 10**7 each. One array is for numbers that go to 89
# and the other is for numbers that go to 1. 
# For the first array, a[i] == True if the number is known to go to 89
# and likewise for b[i] == True. A False entry is tantamount to "no data"
# Each time you do the loopAt89 thing, store each successive number in 
# an array. If you end up at 89, loop through the list and flip the 
# a array at each index so obviously a[89] == True and b[1] == True trivially.
# For each number, you check if its entry is True in either array so that
# you don't need to compute when you don't need to.
# Faster implementation are possible but not worth discussing for the time
# being.



def loopAt89(x):
  sum = x
  while sum != 89 and sum != 1:
    lx = list(str(sum))
    sum = 0
    for i in lx:
      sum += int(i)**2
  if sum == 89:
    return True
  else:
    return False

n = 0
for i in xrange(1, 10**7):
  if loopAt89(i):
    n += 1

print n, "numbers below 10 million will arrive at 89"
