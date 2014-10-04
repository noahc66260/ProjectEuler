from problem24 import permN
from math import *

m = 918273645
for i in range(factorial(9), factorial(9) - factorial(8), -1):
  x = ''.join(str(j) for j in permN(i, 1, 10))
  a = int(x[:4])
  b = int(x[4:])
  if 2*a == b:
    m = int(x)
    break

print m

