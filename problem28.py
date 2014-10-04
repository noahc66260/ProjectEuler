'''
This spiral follows a simple pattern
Suppose we have a running sum, starting at 1 and a value, starting at 1, 
and a level, starting at 2.
If for four iterations we add level to value and value to sum, then
incrementing level by 2, we'll have all the diagonal elements. 
A proof could be written for this but it seems correct
'''

s = 1 # sum
n = 1 # number of elements
v = 1 # value of element we are about to count
l = 2 # level

while n != 2001: # there will be 2 x 1001 - 1 = 2001 elements
  for i in range(4):
    v += l
    s += v
    n += 1
  l += 2

print s
