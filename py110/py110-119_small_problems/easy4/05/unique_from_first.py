list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]


def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)


print(unique_from_first(list1, list2) == {9, 3})
