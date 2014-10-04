''' 
This was easy. I didn't think my solution would be fast enough, but it worked
'''

s = []
for a in range(2, 101):
  for b in range(2, 101):
    e = a**b
    if e not in s:
      s.append(e)

print len(s)
