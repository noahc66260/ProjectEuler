from problem27 import isPrime
from math import *

primes = [i for i in range(10**4) if isPrime(i)]

def is_square(x):
  return (int(sqrt(x)))**2 == x

for i in range(9, primes[-1], 2):
  s = i
  if not isPrime(i):
    flag = False    
    for j in [k for k in range(i) if isPrime(k)]:
      if is_square((i - j)/2):
        flag = True
        break
    if not flag:
      break

print s
