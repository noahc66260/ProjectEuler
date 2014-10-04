def ispalindrome(x):
  s = str(x)
  for i in xrange(len(s) / 2):
     if s[i] != s[-1 - i]:
       return False
  return True

max = 0;
for i in xrange(1000):
  for j in xrange(1000):
    prod = i*j
    if ispalindrome(prod) and prod > max:
      max = prod
print "max is", max
