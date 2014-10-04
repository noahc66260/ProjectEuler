def isCuriousFrac(num, denom):
  """
  Determines if the pair constitute a curious fraction, where
  erroneously canceling out like digits (for multidigit numbers)
  still gets you the correct reduction, such as 
  49/98 = 4/8. Excludes trivial examples, like 30/50 = 3/5.
  It is up to the user to solve the rest of the problem.
  """
  if num == denom:
    return False
  if num % 10 == 0 or denom % 10 == 0:
    return False
  if num % 11 == 0 or denom % 11 == 0:
    return False
  frac = (1.0) * num / denom
  num = str(num)
  denom = str(denom)
  for i in range(2):
    for j in range(2):
      if num[(i + 1) % 2] == denom[(j + 1) % 2]  \
         and \
         float(num[i]) / float(denom[j]) == frac:
          return True
  return False

n = [] 
d = []
for i in range(10, 50):
  for j in range(i, 100):
    if isCuriousFrac(i, j):
      n.append(i)
      d.append(j)

print n
print d

