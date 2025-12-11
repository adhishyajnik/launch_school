"""
Inputs: 2 lists
Outputs: Set

Explicit Rules:
- Function returns a set containing the union of the two input lists' values
- Both arguments will always be lists

Data Structure/s:
- input lists
- convert to set before or after union operation

Algorithm:
- concatenate list_1 and list_2 and coerce the result to a set
- return the resulting set
"""


def union(list_1, list_2):
    return set(list_1 + list_2)


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9})  # True
