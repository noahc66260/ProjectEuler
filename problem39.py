'''
This was a tough one to do efficiently.
The code is self-explanatory, but the idea was to save values beforehand
and make data quick to access rather than recompute. I had a double loop
to find all right triangles and add the perimeter to a list of solutions.
The solution is computed very quickly.
'''


from math import *

squares = [i**2 for i in range(500)]
is_square = [False for i in range(500**2)]
for i in squares:
  is_square[i] = True

solutions = [0 for i in range(1001)] # index is perimeter

for i in range(1, 500):
  for j in range(i, 500):
    hypot_sq = squares[i] + squares[j]
    if hypot_sq < 500**2 and is_square[squares[i] + squares[j]]:
      perim = sqrt(squares[i])  \
              + sqrt(squares[j]) + sqrt(squares[i] + squares[j])
      if perim <= 1000:
        solutions[int(perim)] += 1

print solutions.index(max(solutions))


