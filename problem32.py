'''
We check all permutations of the digits 1 - 9 individually.
For each case, we "cut up" the string into multiplicand, multiplier,
and product. At most there are 28 ways to cut but with some thought
we can reduce it to 4 ways. If we have a pandigital product we check
it against a list of verified pandigital products and add it if
it is not in our set.
'''

from problem24 import permN
from math import *


def panProd(s):
  '''
  Returns a list with all pandigital products.
  s must be a permutation of the numbers 1 - 9 as a string
  '''
  t = []
  i = 4 # apparently our product is exactly four digits
  p = int(s[5:])
  for j in range(1, 5):
    m1 = int(s[:j])
    m2 = int(s[j:5])
    #if mult_table[m1][m2] == p and p not in t:
    if m1*m2 == p and p not in t:
      t.append(p)
  return t


pan = []
f = factorial(9)
for i in range(1, f+1):
  #print i
  s = permN(i, 1, 10)
  
  s = ''.join(str(i) for i in s)
  t = panProd(str(s))
  for j in t:
    if j not in pan:
      pan.append(j)

print sum(pan)
