from problem27 import isPrime

def is_perm(a, b):
  '''
  Returns true if strings a and b are permutations of each other
  '''
  if len(a) != len(b):
    return False
  a = list(a)
  b = list(b)
  a.sort()
  b.sort()
  if a == b:
    return True
  else:
    return False


for i in range(1, 3333):
  for j in range(1000, 10**4 - 2*i):
    if j == 1487: # we've already covered this case
      continue
    a = j
    b = a + 3330
    c = b + 3330
    if isPrime(a) and isPrime(b) and isPrime(c):
      sa = str(a)
      sb = str(b)
      sc = str(c)
      if is_perm(sa, sb) and is_perm(sb, sc) and is_perm(sc, sa):
        break

print a, b, c
