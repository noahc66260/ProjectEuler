
def fac(x):
  if x == 0:
    return 1
  else:
    return x * fac(x-1)

t = []
for digit in str(fac(100)):
  t.append(int(digit))


print sum(t)
