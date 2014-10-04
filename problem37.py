'''
Since there are an infinite number of primes, I'll take it as a given
that there are *only* 11 truncatable primes.
'''

from problem35 import primeList

#i = 15
tp = []
r = 5
while len(tp) < 11:
  tp = []
  is_prime = [False for i in range(10**r)]
  p = primeList(10**r)
  for j in p:
    is_prime[j] = True
  for j in p:
    counter = True
    for k in range(1, len(str(j))): 
      if not is_prime[int(str(j)[k:])]: # truncate left
        counter = False
      if not is_prime[int(str(j)[:-k])]: # truncate right
        counter = False
    if counter and j not in [2, 3, 5, 7]:
      tp.append(j)
  #break
  r += 1

print sum(tp)


  

