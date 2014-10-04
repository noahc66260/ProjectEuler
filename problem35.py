def primeList(n):
  '''
  Returns list of primes below n
  '''
  t = []
  s = [True for i in range(n)]
  s[0] = False
  s[1] = False
  for i in range(len(s)):
    if s[i] == True:
      t.append(i)
      k = i+i
      while k < len(s):
        s[k] = False
        k += i
  return t

def rotateLeft(s, n):
  '''
  Rotates a string to the left by n positions, wrapping around
  to the right.
  '''
  return s[n:] + s[:n]

p = primeList(10**6)
is_prime = [False for i in range(10**6)]
for i in p:
  is_prime[i] = True
circ = []
for x in p:
  #print x
  counter = True
  for i in range(len(str(x))):
    if not is_prime[int(rotateLeft(str(x), i))]:
      counter = False
  if counter:
    circ.append(x)

print len(circ)
