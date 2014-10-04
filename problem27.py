from math import sqrt

def isPrime(x):
  x = abs(x)
  if x == 0 or x == 1:
    return False
  for i in range(2, int(sqrt(x)+1)):
    if x % i == 0:
      return False
  return True

# all primes up to 10**6
primes = [True for i in range(10**6)]
primes[0] = False
primes[1] = False
for i in range(2, len(primes)):
  if primes[i] == True:
    k = i+i
    while k < len(primes):
      primes[k] = False
      k += i

# a slow but accurate function
def quad1(a, b, n):
  return n*n + a*n + b

def sign(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  else:
    return 0

n_sq = [i**2 for i in range(1000)]
n_mult = [[i * j for j in range(1000)] for i in range(1000)]

# a much faster implementation
def quad2(a, b, n):
  return n_sq[n] + sign(a)*n_mult[n][abs(a)] + b


# b must be prime so let's calculate all the primes whose abs val is < 1000
p = [i for i in range(len(primes[:1000])) if primes[i] == True and i > 1]
neg_p = [-i for i in p]
p = p + neg_p
p.sort()


m = 0
ab_prod = 0

for b in p:
  # range of a will depend on b so that our numbers are pos
  if b < 0:
    z = -b
  else:
    z = -999
  for a in range(z, 1000, 2): # a cannot be even
    n = 0
    while primes[quad2(a,b,n)]:
      n += 1
    if m < n:
      m = n
      ab_prod = a*b

print ab_prod
