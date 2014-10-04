#!/usr/bin/python

def divisors(x):
  '''
  Returns list of divisors of integer x, not including x
  '''
  d = []
  for i in range(1,x):
    if x % i == 0:
      d.append(i)
  return d

t = 0
for i in range(10000):
  a = sum(divisors(i))
  b = sum(divisors(a))
  if b == i and i != a:
    t += i

print t
    
