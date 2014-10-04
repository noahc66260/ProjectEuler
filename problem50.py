from problem27 import isPrime

primes = [i for i in range(10**4) if isPrime(i)]
is_prime = [False for i in range(10**4)]
for i in primes:
  is_prime[i] = True

def sumPrime(p, n):
  '''
  Returns a list whose first element is the max number of consecutive
  numbers whose sum is both prime and less than n, and second element 
  is the prime summed to
  '''
  s = sum(p)
  if s < n and isPrime(s):
    return [len(p), s]

  a = sumPrime(p[1:], n)
  b = sumPrime(p[:-1], n)
  if a[0] < b[0]:
    return b
  else:
    return a

#s = sumPrime(primes, 10**4)
#print s

t = 0
flag = False
for i in range(len(primes), -1, -1):
  #if i % 100 == 0:
  #  print i
  for j in range(len(primes) - i + 1):
    p = sum(primes[j:j+i])
    if p < 10**6 and isPrime(p):
      t = i
      flag = True
      break
  if flag:
    break

print p, t
