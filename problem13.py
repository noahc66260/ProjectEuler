fin = open("problem13.txt")

sum = 0
for line in fin:
  line = int(line)
  sum += line

print sum #% 10**40
