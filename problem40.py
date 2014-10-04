'''
Possible to do analytically but easier by computer if you see that
it won't require too much memory
'''

x = [str(i) for i in range(10**6 + 1)]
x = ''.join(x)

s = 1
for i in range(7):
  s *= int(x[10**i])

print s

