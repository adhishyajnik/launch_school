"""
Inputs: list of integers
Outputs: integer greater than or equal to -1

Explicit Rules:
- Function returns an integer such that the sum of the numbers in int_list
  less than that integer index are equal to the sum of the numbers in int_list
  greater than that integer index
- If there is more than one integer that satisfies this requirement, return
  the smallest of those integers
- If there is no integer where this is true, return -1
- The sum of numbers to the left of the first element is 0
- The sum of numbers to the right of the last element is also 0

Implicit Rules:

Data Structure/s:
- list
- int

Algorithm:
- iterate through each idx in a range the length of int_list:
    - if idx is 0:
        - if the sum of int_list from 1 to the end is 0:
            - return idx
    - elif idx is equal to the length of int_list - 1:
        - if the sum of int_list from the beginning to idx is 0:
            - return idx
    - elif the sum of int_list from 0 to idx is equal to
      the sum of int_list from idx + 1 to the end:
        - return idx
- return -1
"""


def equal_sum_index(int_list):
    for idx in range(len(int_list)):
        if idx == 0 and sum(int_list[1:]) == 0:
            return idx
        elif idx == len(int_list) - 1 and sum(int_list[:idx]) == 0:
            return idx
        elif sum(int_list[:idx]) == sum(int_list[idx + 1 :]):
            return idx
    return -1


print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
