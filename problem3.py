import array

def isPrime(n):
  for i in xrange(2,n-1):
    if n % i == 0:
      return False
  return True

#max = 1
#i = 1
num = 600851475143
#num = 13195
#rtnum = int((num)**(.5))
#while i <= rtnum and i <= num:
#  if isPrime(i) and num % i == 0:
#    max = i
#    num = num / i
#  else:
#    i += 1

primes = array.array('i', (1 for i in range(0, int(num**(.5)))))
for i in range(2, len(primes)-1):
  if primes[i] != 0:
    primes[i] = i
    k = 2*i
    while k < len(primes):
      primes[k] = 0
      k += i

max = 1
i = 2
while i <= num and i < len(primes):
  if primes[i] != 0 and num % i == 0:
    max = i
    num /= i
  else:
    i += 1

print "largest prime factor of is", max
