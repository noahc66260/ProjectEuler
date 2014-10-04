for i in range(1, 1000):
  for j in range(1, i):
    if 10**6 - (10**3 * 2 * (j+i)) + 2*j*i == 0:
      a = i
      b = j

c = (a**2 + b**2)**(.5)

def hypoteneuse(a,b):
  return (a**2 + b**2)**(.5)

print "a = %d, b = %d, c = %d" % (a,b,(a**2 + b**2)**(.5))

