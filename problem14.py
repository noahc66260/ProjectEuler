def nCollatz(n):
  sum = 1
  while n != 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3*n + 1
    sum += 1
  return sum

#print "Collatz 13 sequence length is", nCollatz(13)

max = 0
maxCollatz = 0
for x in xrange(1,1000000):
  xCollatz = nCollatz(x)
  if xCollatz > maxCollatz:
    max = x
    maxCollatz = xCollatz
print "max Collatz sequence number is", max
