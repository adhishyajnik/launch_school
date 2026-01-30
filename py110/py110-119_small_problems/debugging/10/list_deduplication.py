"""
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed



We have to generate a new list to store our unique data before iterating
over the list, so that the order of items is preserved. Each time we add
a value from the original list to the new list, we should remove it from
the set of unique values from that list, so that the value doesn't get
added to the new list on future iterations.

We can also do this the opposite way: add a number to the list if it's
not already in a set of numbers that have been added, and then add that
newly-added number to the set.
"""

"""
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_set = set(data)
unique_data = []
for number in data:
    if number in unique_set:
        unique_data.append(number)
        unique_set.discard(number)
print(unique_data == [4, 2, 1, 3])  # order not guaranteed
"""

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_set = set()
unique_data = []
for number in data:
    if number not in unique_set:
        unique_data.append(number)
        unique_set.add(number)
print(unique_data == [4, 2, 1, 3])  # order not guaranteed
