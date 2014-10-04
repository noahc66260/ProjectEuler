from math import *

def is_pent(x):
  return (sqrt(24*x+1) + 1) % 6 == 0

def is_hexa(x):
  return (sqrt(8*x+1) + 1) % 4 == 0

def triangle(x):
  return x * (x + 1) / 2

n = 286
flag = False
while True:
  t = triangle(n)
  if is_pent(t) and is_hexa(t):
    flag = True
  if flag:
    break
  n += 1
  #if n % 100 == 0:
  #  print n

print t
    
