t = 0
num = 0
for i in range(1, 1000):
  r = []
  rem = 1000 % i
  r.append(rem)
  while True:
    rem = (rem * 10) % i
    if rem in r:
      break
    else:
      r.append(rem)
  if t < len(r):
    t = len(r)
    num = i

print num
