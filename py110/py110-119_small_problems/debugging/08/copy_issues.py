import copy

"""
original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])


The copy.copy function creates a shallow copy of objects, so objects in data structures
nested within the copy are shared between the original and the copy.

Rather than reassigning nested values, we can simply reassign top-level elements
of the original list, which are not shared with the copy.

Alternately, we could make a deep copy of the original list and then we would
be able to reassign nested elements in either list without affecting the other,
because all nested data structures would be duplicated.
"""

# solution 1
"""
original = [[1], [2], [3]]
copied = copy.copy(original)

original[0] = [99]

print(copied[0] == [1])
"""

# solution 2

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])
