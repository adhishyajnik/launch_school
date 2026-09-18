"""
Problem: Write a function that returns a new list where the input
list's first element is at the end of the returned list.

Inputs: Any object
Outputs: List

Explicit Rules:
- Function should return a new list, not mutate the input
- The returned list should be the same as the input list, except
  that the input list's first element is the last element of the
  returned list
- If the input is an empty list, return an empty list
- If the input is not a list, return None

Implicit Rules:
- Input lists can contain multiple object types
- Unclear whether input list elements should point to different
  objects in memory than the output list. Will implement without this feature.

Data Structure/s:
- List

Algorithm:
- If the input is not a list, return None
- Otherwise initialize a new list from the
  slice of input list starting at index 1
- Then append the first element from input list to the new list and return it
"""


def rotate_list(input):
    if not isinstance(input, list):
        return None
    elif input == []:
        return []

    output = input[1:] + [input[0]]

    return output


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(["a", "b", "c"]) == ["b", "c", "a"])
print(rotate_list(["a"]) == ["a"])
print(rotate_list([1, "a", 3, "c"]) == ["a", 3, "c", 1])
print(rotate_list([{"a": 2}, [1, 2], 3]) == [[1, 2], 3, {"a": 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
