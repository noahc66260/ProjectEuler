def divisors(x):
  '''
  Get proper divisors of x
  '''
  d = []
  for i in range(1,x):
    if x % i == 0:
      d.append(i)
  return d

def isAbundant(x):
  if sum(divisors(x)) > x:
    return True
  else:
    return False

t = []
for i in range(1, 28123+1):
  if isAbundant(i):
    t.append(i)

s = [i for i in range(28123+1)]
for i in range(len(t)):
  for j in range(i, len(t)):
    if t[i] + t[j] < len(s):
      s[t[i] + t[j]] = 0

print sum(s)
