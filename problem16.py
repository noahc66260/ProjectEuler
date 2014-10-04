from math import *

t = list(str(2**1000))
for i in range(len(t)):
  t[i] = int(t[i])

print sum(t)
