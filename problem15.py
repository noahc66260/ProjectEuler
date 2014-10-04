"""
No code is necessary. We note that we can only move down or to the right.
We have 20 moves down, 20 to the right, 40 total. This is the equivalent
to 40 choose 20.
"""

from math import *
print factorial(40) / (factorial(20) * factorial(20))
