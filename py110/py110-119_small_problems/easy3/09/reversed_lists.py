"""
Inputs: lst (list)
Outputs: lst

Explicit Rules:
- Function reverses the elements of 'lst' in place (mutating) and returns the same object
- The list.reverse method is not available, nor is slicing with a step of -1

Implicit Rules:
- 'lst' can contain integers or strings, or be empty
- if 'lst' is empty, the function returns it as is (the same object)
- the function does not reverse the order of characters in strings, it only reverses the order of list elements

Data Structure/s:
- lst list
- integer and string elements in list

Algorithm:
- initialize 'flipped' as an empty list
- remove the last element of 'lst' and append it to 'flipped'
    - repeat this until 'lst' is empty
- iterate through each 'elem' in 'flipped'
    - append 'elem' to 'lst'
return 'lst'

Flipped as list comprehension (I'm not sure if using range with start, stop, step arguments is allowed):
    - Select: 'lst'['idx']
    - Collection Element: 'idx'
    - Collection: a range starting at the length of 'lst' -1, ending at -1, with a step of -1
        (This calls the indices of 'lst' in reverse order)
    - Condition: none
"""


def reverse_list(lst):
    flipped = []
    while lst:
        flipped.append(lst.pop())
    for elem in flipped:
        lst.append(elem)
    return lst


def reverse_list2(lst):
    flipped = [lst[idx] for idx in range(len(lst) - 1, -1, -1)]
    lst.clear()
    for elem in flipped:
        lst.append(elem)
    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])  # True
print(list1 is result)  # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ["e", "d", "c", "b", "a"])  # True
print(list2 is result2)  # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ["abc"])  # True
print(list3 is result3)  # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])  # True
print(list4 is result4)  # True
