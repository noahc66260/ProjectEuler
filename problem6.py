# I happen to know the formulas for the sum of squares and the sum of 
# consecutive numbers.

n = 100

def sumOfSquares(n):
  return n * (n + 1) * (2*n + 1) / 6

def squareOfSum(n):
  return n**2 * (n+1)**2 / 4

print "The difference is", squareOfSum(n) - sumOfSquares(n)
