
s = 0
for n in range(1, 1001):
  s += n**n
  s %= 10**10

print s
