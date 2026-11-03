"""
Inputs: list of numbers (int and/or float)
Outputs: number (int or float)

Explicit Rules:
- Function returns the number in num_list that occurs only once;
- num_list contains the same number multiple times, and one occurence of a
  different number
- num_list will always contain at least 3 numbers, and 1 will always be
  different from the others

Implicit Rules:
- num_list may contain integers and/or floats

Data Structure/s:
- list
- set

Algorithm:
- set unique_nums to num_list converted to a set and then to a list
- if the first number in unique_nums occurs more than once in num_list:
    - return the second number in unique_nums
- else:
    - return the first number in unique_nums
"""


def what_is_different(num_list):
    unique = list(set(num_list))
    return unique[1] if num_list.count(unique[0]) > 1 else unique[0]


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
