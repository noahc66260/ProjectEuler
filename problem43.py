from problem24 import permN
from math import *

def substr_div(n):
  '''
  For a 0-9 pandigital number, returns true if
  d_2 d_3 d_4 % 2 == 0
  d_3 d_4 d_5 % 3 == 0
  d_4 d_5 d_6 % 5 == 0
  d_5 d_6 d_7 % 7 == 0
  d_6 d_7 d_8 % 11 == 0
  d_7 d_8 d_9 % 13 == 0
  d_8 d_9 d_10 % 17 == 0
  where d_i is the ith digit, starting at d_1
  '''
  n = str(n)
  if len(n) != 10:
    n = '0' + n

  if int(n[1:4]) % 2 != 0:
    return False
  if int(n[2:5]) % 3 != 0:
    return False
  if int(n[3:6]) % 5 != 0:
    return False
  if int(n[4:7]) % 7 != 0:
    return False
  if int(n[5:8]) % 11 != 0:
    return False
  if int(n[6:9]) % 13 != 0:
    return False
  if int(n[7:]) % 17 != 0:
    return False

  return True


s = []
for i in range(factorial(10), -1, -1):
  t = int(''.join([str(j) for j in permN(i, 0, 10)]))
  if substr_div(t):
    s.append(t)

#print s
print sum(s)
