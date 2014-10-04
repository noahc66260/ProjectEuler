'''
Wow this was difficult. At a minimum I may have spent 4 hours.
I worked at this analytically for a while. The "best" way I have
to think about this is that D = |P_k - P_j| must be a pentagonal number.
Suppose P_j < P_k. Then D + P_j and D + 2*P_j is pentagonal.
I made a list of pentagonal numbers and checked as many instances as
possible for a given D. Unfortunately I have no analytical way to show
that, say, we don't need to compute an infinite number of cases for 
each instance of D. I think I got lucky on this question. Note sure
how others went about it. The computation took maybe 10 minutes until
it spit out the appropriate value, much to my surprise. 

Update: 
  So I took a look at the thread discussing this question after solving it.
  Others did what I did, but used the direct way to calculate if a number
  is triangular from wikipedia. I was not aware of this formula.
  My algorithm was so damn slow because searching through a list
  is O(n), so my problem scaled poorly. I changed my code to calculate
  if a number is pentagonal directly and it runs faster, but still no
  word on a convincing argument for not testing an infinite number
  of cases :(
'''


pent = [n*(3*n - 1)/2 for n in range(1, 3000)]

def is_pent(x):
  f = (.5 + sqrt(.25 + 6*x))/3
  if f - int(f) == 0:
    return True
  else:
    return False

from math import *

d_reached = False
for diff in pent:
  #print "checking", diff
  for little in pent:
    big = diff + little
    if is_pent(big):
      if is_pent(big + little):
        print "distance =", big - little
        d_reached = True
        break
  if d_reached:
    break
