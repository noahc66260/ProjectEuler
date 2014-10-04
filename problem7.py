import array

# I am guessing the 10001th prime is less than 10 million
count = 0
primes = array.array('i', (1 for i in range(10**7)))
for i in range(2, len(primes) - 1):
  if primes[i] != 0:
    count += 1
    if count == 10001:
      break
    primes[i] = i
    k = i + i
    while k < len(primes):
      primes[k] = 0
      k += i

if count == 10001:
  print "10001th prime is", i
else:
  print "didn't find the 10001th prime :("

