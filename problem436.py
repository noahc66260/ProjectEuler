# wow this is a hard problem. I don't see this computer having enough
# power to do the simulation over >> 10**10 games so this must be
# done analytically, but doing this analytically is hard and long.
# Basically you need to calculate the expected score for player 1 and
# separate each case (one throw, two throws, ..., n throws) and then
# integrate over the possible values for your variable.
# THEN you need to do it again but this time to find the expected
# overshoot from 1 for the last throw with is again an integral of sums.
# THEN you need to do it again for the second player in a new way to
# calculate their score.
# But these are infinite sums (yeah... eventually you will truncate).
# The point being that this involves a lot of computation, pretty much
# must be done analytically, and is very long and arduous. 
# I"m just going to save this stuff for later

from random import uniform # is this the right fn?

games = 10 ** 8
p1 = 0
p2 = 0

for x in xrange(games):
  s = 0
  while (s < 1):
    x = uniform(0,1)
    s += x
  while (s < 2):
    y = uniform(0,1)
    s += y
  if x > y:
    p1 += 1
  elif x < y:
    p2 += 1
  else:
    continue

print "probability player two wins is %.10f" % (float(p2) / games)
