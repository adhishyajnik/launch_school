"""
data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)



This throws an error because the set changes size while iterating
over it, and because sets are unordered collections, it cannot simply
iterate to the next index after an element is removed.

We must generate a new set using either the for/if structure or a set comprehension.
"""

data_set = {1, 2, 3, 4, 5}

print({item for item in data_set if item % 2 == 0})
