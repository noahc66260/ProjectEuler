alphabet = " abcdefghijklmnopqrstuvwxyz"

fin = open("names.txt")
line = fin.readline()
t = line.split(',')
for i in range(len(t)):
  t[i] = t[i][1:-1]

t.sort()

s = 0 # our running sum
for i in range(len(t)):
  r = 0 # sum of all letters in word
  for j in range(len(t[i])):
    #print t[i][j]
    r += alphabet.index(t[i][j].lower())
  s += r * (i + 1)

print s

