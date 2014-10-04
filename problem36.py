from math import *

def isPalindrome(s):
  '''
  Returns true if the string s is a palindrome
  '''
  return s == s[-1::-1]

def decimalToBinary(n):
  '''
  Converts a decimal integer to binary
  '''
  if n == 0:
    return 0
  s = []
  upper = int(log(n, 2))
  for i in range(upper, -1, -1):
    t = 2**i
    if n < t:
      s.append(0)
    else:
      s.append(1)
      n -= t
  return int(''.join(str(i) for i in s))

p = []
for i in range(1, 10**6):
  if isPalindrome(str(i)) and isPalindrome(str(decimalToBinary(i))):
    p.append(i)

print sum(p)

