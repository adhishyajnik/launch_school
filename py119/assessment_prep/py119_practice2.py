"""
Inputs: list of integers
Outputs: integer or None

Explicit Rules:
- Function returns the smallest sum of 5 consecutive integers in lst
  if lst length is at least 5, otherwise returns None

Implicit Rules:
- lst may contain positive and negative integers, as well as 0

Data Structure/s:
- List

Algorithm:
- Return None if lst length is less than 5
- Return minimum value in list comprehension that stores the sum of idx 0-4,
  1-5, 2-6... lst length - 5:lst length
"""


def minimum_sum(lst):
    return (
        None
        if len(lst) < 5
        else min([sum(lst[idx : idx + 5]) for idx in range(len(lst) - 4)])
    )


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
