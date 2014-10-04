# This question is ripping my cock off. I can code a solution but it's
# intolerably slow to the point that I don't think this is how it should
# be done. I'm leaving it for now.

def reverseInt(n):
  listn = list(str(n))
  listn.reverse()
  return int(''.join(listn))

def everyDigitOdd(n):
  listn = list(str(n))
  for num in listn:
    if int(num) % 2 == 0:
      return False
  return True

def isReversible(n): # n should be a list of integers
  if n[-1] == 0:
    return False
  carryover = False
  for i in xrange((len(n) + 1)/2):
    sum = n[i] + n[-1-i]
    if carryover and sum % 2 != 0:
      return False
    if not carryover and sum % 2 == 0:
      return False
    if sum > 9:
      carryover = True
    else:
      carryover = False
  return True


#sum = 0
#for n in xrange(1,10**3):
#  if (everyDigitOdd(n + reverseInt(n)) and 
#      len(list(str(n))) ==  len(list(str(reverseInt(n))))):
#    sum += 1

#count = 0
#for n in xrange(1,10**3):
#  if n % 10 == 0:
#    continue
#  forward = str(n)
#  if int(forward[0]) + int(forward[-1]) % 2 == 0:
#    continue
#  reverse = forward[::-1] 
#  sum = int(forward) + int(reverse)
#  if everyDigitOdd(sum):
#    count += 1

count = 0
for n in xrange(1,10**6):
  listn = [int(x) for x in str(n)]
  if isReversible(listn):
    count += 1

print "There are", count, "numbers below 10**x with the desired property"
