from math import *

def permN(x, n1, n2):
  ''' 
  Finds xth permutation from integers [n1,n2) in lexographic order.
  n1 must be less than n2.
  Returns a list with the permutation.
  1 <= x <= (n2 - n1)!
  '''
  t = x
  digits = range(n1, n2)
  #print len(digits)
  p = []
  for i in range(n2 - n1 - 1, 0, -1):
    #for j in range(len(digits)):
    for j in range(i+1):
      if j*factorial(i) <= t and t <= (j+1)*factorial(i):
        p.append(digits[j])
        t = t - j*factorial(i)
        del digits[j]
        break
  for i in range(len(digits)):
    p.append(digits[i])
  return p

print int(''.join(str(i) for i in permN(10**6, 0, 10)))

