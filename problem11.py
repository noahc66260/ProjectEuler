fin = open("problem11.txt")
matrix = [range(20) for i in range(20)]

row = 0
for line in fin:
  t = line.split(' ')
  for col in range(len(t)):
    matrix[row][col] = int(t[col])
  row += 1

def valid_index(rows, cols, i, j):
  if i < 0 or rows <= i or j < 0 or cols <= j:
    return False
  return True

def dfs(matrix, product, i, j, depth):
  if depth > 4:
    return product
  product *= int(matrix[i][j])
  max = 0
  for k in range(i-1, i+2):
    for l in range(j-1, j+2):
      if valid_index(20, 20, k, l) and k != i and l != j:
        prod = dfs(matrix, product, k, l, depth + 1)
        if prod > max:
          max = prod
  return max

#max = 0;
#for i in range(20):
#  for j in range(20):
#    prod = dfs(matrix, 1, i, j, 1)
#    if prod > max:
#      max = prod
#print max

# first we do up direction
max = 0;
for i in range(20 - 3):
  for j in range(20):
    prod = matrix[i][j] * matrix[i+1][j] * matrix[i+2][j] * matrix[i+3][j]
    if prod > max:
      max = prod

# now we do sideways
for i in range(20):
  for j in range(20 - 3):
    prod = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
    if prod > max:
      max = prod

# now we do diagonal with positive y-slope
for i in range(3, 20):
  for j in range(20 - 3):
    prod = matrix[i][j] * matrix[i-1][j+1] * matrix[i-2][j+2] * matrix[i-3][j+3]
    if prod > max:
      max = prod

# now we do diagonal with negative y-slope
for i in range(20 - 3):
  for j in range(20 - 3):
    prod = matrix[i][j] * matrix[i+1][j-1] * matrix[i+2][j-2] * matrix[i+3][j-3]
    if prod > max:
      max = prod

print max
