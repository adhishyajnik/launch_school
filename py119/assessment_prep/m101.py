"""
Write a function that rotates a list by moving the first element to the end of
the list. Do not modify the original list; return a new list instead.

    If the input is an empty list, return an empty list.
    If the input is not a list, return None.

Review the test cases below, then implement the solution accordingly.

Inputs: list (or any other object)
Outputs: list or None

Explicit Rules:
- Function returns a new list object, not the same one it was passed
- Function moves the first list element to the end of the list
- Function returns None if it was not passed a list
- Function returns an empty list if it was passed an empty list

Implicit Rules:
- Function does not mutate the list passed to it; it returns a new list object

Data Structure/s:
- List
- None

Algorithm:
- if lst is not a list, return None
    - we'll need to use isinstance() for this
- if lst is empty, return []
- set output to a list comprehension that stores each list element from lst
  if its index is not 0
- then append the index-0 element from lst to output
- return lst
"""


def rotate_list(lst):
    if lst == []:
        return []
    elif isinstance(lst, list) == False:
        return None

    output = lst[1:]
    output.append(lst[0])
    return output


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(["a", "b", "c"]) == ["b", "c", "a"])
print(rotate_list(["a"]) == ["a"])
print(rotate_list([1, "a", 3, "c"]) == ["a", 3, "c", 1])
print(rotate_list([{"a": 2}, [1, 2], 3]) == [[1, 2], 3, {"a": 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)  # noqa
print(rotate_list(1) == None)  # noqa

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
