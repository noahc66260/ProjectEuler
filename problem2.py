def nextFib(a,b):
  return a + b

a = 1
b = 2
sum = 0
while b < 4 * 10**6:
  if b % 2 == 0:
    sum += b
  c = nextFib(a,b)
  a = b
  b = c

print "sum of even fib terms below 4 * 10**6 is", sum
