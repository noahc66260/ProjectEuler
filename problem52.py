def sameDigits(x, y):
  sx = str(x)
  sy = str(y)
  if len(sx) != len(sy):
    return False
  else:
    sx = list(sx)
    sy = list(sy)
    sx.sort()
    sy.sort()
    if sx == sy:
      return True

#print "sameDigits(1234, 4213) is", sameDigits(1234, 4213)
i = 1
while True:
  if (sameDigits(i, 2*i) and 
      sameDigits(i, 3*i) and 
      sameDigits(i, 4*i) and 
      sameDigits(i, 5*i) and 
      sameDigits(i, 6*i)):
      # do
      break
  else:
      i += 1

print "try", i
