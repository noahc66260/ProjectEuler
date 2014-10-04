year = 1900
month = 1
day = 1
weekday = 1 # 0 is Sunday

def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  return False

count = 0
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while (year != 2000 or month != 12 or day != 31):
  if weekday == 0 and day == 1 and year >= 1901:
    count += 1

  if month == 2 and day == days_in_month[month-1] and isLeapYear(year):
    day += 1
  elif month == 12 and day == days_in_month[month-1]:
    day = 1
    month = 1
    year += 1
  elif day >= days_in_month[month-1]:
    day = 1
    month += 1
  else:
    day += 1

  weekday = (weekday + 1) % 7

print count
