"""
Inputs: two lists
Outputs: list

Explicit Rules:
- Function combines two lists such that the elements alternate from list 1 and list 2
- Both input lists are non-empty
- Both input lists are of the same length

Implicit Rules:
- List elements can be anything

Data Stucture/s:
- 2 input lists
- 1 output list

Algorithm:
- initialize 'output' to an empty list
- iterate through every 'i' in a range the length of list 1
    - extend 'output' with a list containing 2 elements:
        - the element at index 'i' from list 1
        - the element at index 'i' from list 2
- return 'output'
"""


def interleave(list1, list2):
    output = []
    for i in range(len(list1)):
        output.extend([list1[i], list2[i]])
    return output


def interleave_zip(list1, list2):
    output = []
    zlist = list(zip(list1, list2))
    for tup_pair in zlist:
        output.extend(tup_pair)
    return output


list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)  # True
