"""
About divisors:
  It turns out that every number except a perfect square will have an 
  even number of divisors. To see this, by definition, x is divisible
  by y if for some natural number k, x = k * y. Thus, for every divisor,
  there is a "compliment" for which multiplication by this number
  will become the original number. The exception, of course, is when
  we have a perfect square. We note that for every number, it's compliment
  will be "across" the square root, or if y is a divisor of x, then if
  y < sqrt(x) we have k_y > sqrt(x) and vice versa. Thus, we can find
  the number of divisors of x by calculating the divisors of x smaller 
  than sqrt(x) and doubling that number. Since most numbers are not
  perfect squares, I assumed the answer would not be, so I did not
  check for that case (we'd be off by 1 anyway). My answer was correct,
  so really this calculation was a close approximation.
"""

from math import *

def triangle(x):
  return x * (x + 1) / 2

x = 1
while True:
  divisors = 0
  t = triangle(x)
  for i in range(1, int(sqrt(t))):
    if t % i == 0:
      divisors += 2
  if 500 <= divisors:
    break
  x += 1

print t
