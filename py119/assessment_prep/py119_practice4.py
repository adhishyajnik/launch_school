"""
Inputs: list of integers
Outputs: tuple of 2 integers

Explicit Rules:
- Function returns a tuple containing the 2 integers from lst that are
  closest together in value
- If there are multiple pairs equally close together, function returns the first
  pair that occurs in the list

Implicit Rules:
- Function will only be passed a valid list of integers

Data Structure/s:
- list
- tuple

Algorithm:
- create a list of tuples of every possible pair of integers in lst

- tuple_list = []
- iterate through each start_idx in a range the length of lst - 1:
    - iterate through each end_idx in a range from 1 to the length of lst
        - append a tuple containing lst[start_idx] & lst[end_idx] to tuple_list
- dif_list = []
- iterate through each tuple in tuple_list:
    - append the absolute value of tuple[0] - tuple[1] to dif_list
- min_dif = min(dif_list)
- min_idx = dif_list.index(min_dif)
- return tuple_list[min_idx]
"""


def closest_numbers(lst):
    tuple_list = [
        (lst[start_idx], lst[end_idx])
        for start_idx in range(len(lst) - 1)
        for end_idx in range(start_idx + 1, len(lst))
    ]
    dif_list = [abs(tup[0] - tup[1]) for tup in tuple_list]
    min_dif = min(dif_list)
    min_idx = dif_list.index(min_dif)
    return tuple_list[min_idx]


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
