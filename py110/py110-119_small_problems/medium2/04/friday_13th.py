"""
Some people believe that Fridays that fall on the 13th day of the month are
unlucky days. Write a function that takes a year as an argument and returns the
number of Friday the 13ths in that year. You may assume that the year is greater
than 1752, which is when the United Kingdom adopted the modern Gregorian
Calendar. You may also assume that the same calendar will remain in use for the
foreseeable future.

Input: integer
Output: integer

Explicit Rules:
- function takes a year as input and returns the number of Fridays that year
  on which the date was the thirteenth of any month

Implicit Rules:
- return value will always be 0 or greater
- input value will always be greater than 1752

Data Structure/s:
- datetime object
- integer
- string

Algorithm:
- initialize unlucky_days to 0
- loop through each month of the year argument
    - if the 13th of this month falls on a Friday:
        - increment unlucky_days
- return unlucky_days
"""

from datetime import date


def friday_the_13ths(y):
    return sum(1 for m in range(1, 13) if date(y, m, 13).weekday() == 4)


print(friday_the_13ths(1986) == 1)  # True
print(friday_the_13ths(2015) == 3)  # True
print(friday_the_13ths(2017) == 2)  # True
