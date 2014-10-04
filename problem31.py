'''
This is a dynamic programming problem.

What I started with is an 8 x 201 matrix. The entry (i, j) should
represent the max combos for making j pence from coins no larger
than i, where i = 0 is 200p, i = 1 is 100p, ... i = 7 is 1 p.
We start by filling in the bottom row, b/c obviously if we have
only one kind of coin we have only one way to make combinations.
Then we go from bottom to top, filling in each row. We compute the
grid space (i,j) to summing (i+1, j), (i+1, j - k*currency[i]), ...
as long as j - k*currency[i] represents a valid index. That's 
our way of saying, use 0 large coins and see how max combo with
smaller coins only, use 1 large coin and see max combo with 
the remainder in smaller coins, ... 

In the end we'll have our answer in combos[0, 200], which is the
grid space for the max combos of coins if our largest coin is 200p
and we are trying to get to 200p.
'''


currency = [200, 100, 50, 20, 10, 5, 2, 1]
# 0 for 200p, ..., 7 for 1p
combos = [[0 for i in range(201)] for j in range(8)]
for j in range(201):
  combos[7][j] = 1
for i in range(6, -1, -1):
  for j in range(0, 201):
    for k in range(0, 201): # not efficient
      if 0 <= j - k*currency[i]: 
        combos[i][j] += combos[i+1][j - k*currency[i]]

print combos[0][200]
