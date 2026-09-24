"""
Write a function that takes two sorted lists as arguments and returns a new list
that contains all the elements from both input lists in ascending sorted order.
You may assume that the lists contain either all integer values or all string
values.

You may not provide any solution that requires you to sort the result list. You
must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

Inputs: 2 lists
Outputs: new list of elems from both lists, sorted

Explicit Rules:
- Function must return a new list; don't mutate input lists
- Function cannot use sorted() or list.sort()
- Elements from both lists should be top-level elements of the returned list,
  i.e. no nested lists in the returned list

Implicit Rules:
- Function will only be passed 2 input lists
- Input lists will contain the same types of objects (all ints or all strs)
- Input lists can be empty; if both are empty, the returned list is empty too
- Input lists may not be the same length as each other

Data Structure/s:
- list
- int
- str

Algorithm:
- initialize an empty output list
- unpack the input lists into a combined list
- while combined still has elements:
    - find the index of the smallest element in combined
    - pop the element at that index from combined and append it to output list
    - pop the smallest element from combined and append it to output list
- return output list
"""


def case_insensitive(elem):
    return str(elem).casefold()


def merge1(lst1, lst2):
    return sorted([*lst1, *lst2], key=case_insensitive)


def merge(lst1, lst2):
    ordered, unordered = [], [*lst1, *lst2]
    while unordered:
        min_elem = min(unordered, key=case_insensitive)
        min_idx = unordered.index(min_elem)
        ordered.append(unordered.pop(min_idx))
    del unordered
    return ordered


# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ["Alice", "Kim", "Pete", "Sue", "BOny"]
names2 = ["Bonnie", "Rachel", "Tyler"]
names_expected = ["Alice", "Bonnie", "BOny", "Kim", "Pete", "Rachel", "Sue", "Tyler"]
print(merge(names1, names2) == names_expected)

# The following example should print False
print(merge(names1, names2) == names1 or merge(names1, names2) == names2)
