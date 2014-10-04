fib = {}
fib[1] = 1
fib[2] = 1
t = 1

i = 3
while len(str(fib[t])) < 1000:
  fib[i] = fib[i-1] + fib[i-2]
  t = i 
  i += 1

print t
