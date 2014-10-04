alphabet = " abcdefghijklmnopqrstuvwxyz"

def hash_word(s):
  '''
  Sums the indices the words in the letter starting at 1
  '''
  t = 0
  for i in s:
    t += alphabet.index(i.lower())
  return t


fin = open('words.txt')
line = fin.readline()
line = line.split(',')

for i in range(len(line)):
  line[i] = line[i][1:-1]

is_triangle = [False for i in range(1000)]
k = 1
while k*k + k < 2*len(is_triangle):
  is_triangle[(k*k + k)/2] = True
  k += 1

count = 0
for i in line:
  if is_triangle[hash_word(i)]:
    count += 1

print count

