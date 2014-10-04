# Suppose we have an n digit number. Since each digit is less than 10,
# we see that the sum of the fifth powers of all the digits is less
# than (n * 10**5). Likewise, we see that any n digit integer will
# always be greater than 10**(n-1). Hence we do not need to check
# numbers such that (n * 10**5) < 10**(n-1). Taking the log of both
# sides and solving for n we see that the inequality is true for 
# n >= 7, which is to say we need only check numbers between 2 and 
# 10**7 - 1 (up to six digit numbers)

def digitFifthPowers(x):
  s = str(x)
  sum = 0
  for i in xrange(len(s)):
    sum += int(s[i]) ** 5
  if sum == x:
    return True
  else:
    return False

sum = 0
for x in xrange(2, 10**7 - 1):
  if digitFifthPowers(x):
    sum += x
print "sum of all numbers whose sum of digits to the fifth power"
print "equal that number is", sum
