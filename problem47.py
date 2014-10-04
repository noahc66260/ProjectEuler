'''
This code will take several minutes to get the answer, which is around
134034 I believe.
'''

def primeFactors(x):
  '''
  Returns a list of the prime factors of x, where each element is 
  a list containing a single prime factor.
  Ex. primeFactor(10) returns [[2], [5]]
  and primeFactor(20) returns [[2,2], [5]]
  '''
  i = 2
  t = []
  while 1 < x:
    r = 0
    while x % i == 0:
      x = x / i
      r += 1
    if 0 < r:
      t.append([i for j in range(r)])
    i += 1

  return t

a = primeFactors(644)
b = primeFactors(645)
c = primeFactors(646)

for i in a:
  if i in b or i in c:
    print 'prime factors not distinct'

i = 2
t = [[] for i in range(4)]
while True:
  flag = True
  if i % 100 == 0:
    print i
  t = [[] for k in range(4)]
  for j in range(len(t)):
    t[j] = primeFactors(i + j) 
    if len(t[j]) != len(t):
      break
  if len(t[-1]) != len(t):
    i += 1
    continue
  for j in range(len(t)):
    for a in t[j]:
      for k in range(j+1, len(t)):
        if a in t[k]:
          flag = False
  if flag:
    break
  i += 1

print i, i+1, i+2, i+3
