"""
Inputs: two lists
Outputs: set

Explicit Rules:
- Convert each list to a set
- Return a new set that is the union of both sets

Data Structure/s:
- lists
- sets
- output set

Algorithm:
- Convert each list to a set
- Return the union of the two resulting sets
"""

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]


def merge_sets(lst1, lst2):
    return set(lst1) | set(lst2)


print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
