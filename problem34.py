'''
It is easy to see that for any number greater than 7*(9!), the number
cannot be the sum of the factorial of its digits. Thus, we check
all numbers up to this limit
'''
from math import *

fac = {}
for i in range(10):
  fac[i] = factorial(i)

def sumFacDigits(n):
  '''
  Returns the sum of the factorial of the digits of n
  '''
  n = list(str(n))
  for i in range(len(n)):
    n[i] = fac[int(n[i])]
  return sum(n)


s = []
limit = 7 * fac[9]
for i in range(limit):
  #print i
  if i == 1 or i == 2:
    continue
  if i == sumFacDigits(i):
    s.append(i)

print sum(s)

