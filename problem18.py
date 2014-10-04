'''
This is really a dynamic programming problem. Basically we save values
for optimal paths starting from the bottom and going up. i.e. given
a node with children representing optimal paths we can determine
the optimal path for that particular node (since it must choose one
of those paths). And repeat inductively.
'''

fin = open("problem18.txt")

tree = [range(i) for i in range(1,16)]
row = 0
for line in fin:
  t = list(line.split(' '))
  for i in range(len(t)):
    tree[row][i] = int(t[i])
  row += 1

paths = [range(i) for i in range(1,16)]
for i in range(len(tree[-1])):
  paths[-1][i] = tree[-1][i]

for i in range(len(tree) - 2, -1, -1):
  for j in range(len(paths[i])):
    if paths[i+1][j] > paths[i+1][j+1]:
      paths[i][j] = tree[i][j] + paths[i+1][j]
    else:
      paths[i][j] = tree[i][j] + paths[i+1][j+1]

print paths[0][0]
