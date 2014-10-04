sum = 0
ones = {};
ones[0] = 0
ones[1] = 3
ones[2] = 3
ones[3] = 5
ones[4] = 4
ones[5] = 4
ones[6] = 3
ones[7] = 5
ones[8] = 5
ones[9] = 4
ones[10] = 3
ones[11] = 6
ones[12] = 6
ones[13] = 8
ones[14] = 8
ones[15] = 7
ones[16] = 7
ones[17] = 9
ones[18] = 8
ones[19] = 8
ones[20] = 6
for i in range(10):
  ones[20 + i] = ones[20] + ones[i]
ones[30] = 6
for i in range(10):
  ones[30 + i] = ones[30] + ones[i]
ones[40] = 5
for i in range(10):
  ones[40 + i] = ones[40] + ones[i]
ones[50] = 5
for i in range(10):
  ones[50 + i] = ones[50] + ones[i]
ones[60] = 5
for i in range(10):
  ones[60 + i] = ones[60] + ones[i]
ones[70] = 7
for i in range(10):
  ones[70 + i] = ones[70] + ones[i]
ones[80] = 6
for i in range(10):
  ones[80 + i] = ones[80] + ones[i]
ones[90] = 6
for i in range(10):
  ones[90 + i] = ones[90] + ones[i]
for i in range(1, 1001):
  sum += ones[i % 100]
  if i > 99 and i != 1000:
    sum += ones[i / 100] + 7 # hundred
  if i % 100 != 0 and i > 99:
    sum += 3 # and
  if i == 1000:
    sum += ones[1] + 8 # thousand

print sum
