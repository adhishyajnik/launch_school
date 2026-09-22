"""
Write a function that computes the difference between the square of the sum of
the first count positive integers and the sum of the squares of the first count
positive integers.

Inputs: integer
Outputs: integer

Explicit Rules:
- function returns the result of subtracting
  the sum of the first n integers squared from
  the squared sum of the first n integers
  i.e. (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

Implicit Rules:
- the larger n is, the larger the returned difference should be
- if n is 1, the returned difference is 0

Data Structure/s:
- int
- range

Algorithm:
- sum all integers from 1 to n
- square the sum and assign it to nsum_squared
- sum the square of each integer from 1 to n and assign it to nsquares_sum
- return nsum_squared - nsquares_sum

Sub-algos:
Sum all integers from 1 to n
- initialize sum to 0
- loop through each number in a range from 1 to n + 1
    - add number to sum

Sum the square of each integer from 1 to n and assign it to nsquares_sum
- initialize nsquares_sum to 0
- loop through each number in a range from 1 to n + 1:
    - add number**2 to nsquares_sum
"""


def sum_square_difference(n):
    return sum(range(n + 1)) ** 2 - sum(num**2 for num in range(n + 1))


print(sum_square_difference(3) == 22)  # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)  # True
print(sum_square_difference(1) == 0)  # True
print(sum_square_difference(100) == 25164150)  # True
