"""
Inputs: int_list (list)
Outputs: integer

Explicit Rules:
- Function returns the average of all integers in 'int_list' rounded down to the integer component
- 'int_list' is never empty
- 'int_list' will only contain positive integers

Implicit Rules:
- 'int_list' may contain only 1 integer element, in which case the result is equal to that element

Data Structure/s:
- input list
- integers

Algorithm:
- Return the sum of the integers in 'int_list' floor-divided by its length
"""


def average(int_list):
    return sum(int_list) // len(int_list)


print(average([1, 5, 87, 45, 8, 8]) == 25)  # True
print(average([9, 47, 23, 95, 16, 52]) == 40)  # True
print(average([7]) == 7)  # True
