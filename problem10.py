import array

primes = array.array('i', (i for i in xrange(2*10**6)))

primes[1] = 0
for i in xrange(2, 2*10**6):
  k = i + i
  while k < len(primes):
    primes[k] = 0
    k += i

print "sum of first 2*10**6 primes is", sum(primes)
