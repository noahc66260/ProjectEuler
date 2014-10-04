'''
No nine digit pandigital number is prime because the sum of the digits is 45.
Likewise for eight, but not for seven.
'''


from problem24 import permN
from problem27 import isPrime
from  math import *


m = 0

for i in range(factorial(8), 0, -1):
  n = ''.join([str(j) for j in permN(i, 1, 8)])
  if isPrime(int(n)) and m < int(n):
    m = int(n)

print m


