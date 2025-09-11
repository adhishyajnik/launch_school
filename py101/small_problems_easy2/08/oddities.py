def oddities(list_):
    return [ odd_elem for elem, odd_elem in enumerate(list_) if elem % 2 == 0 ]

def odd_slicing(list_):
    return list_[::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities([1, 2, 3, 4]) == [1, 3])
print(oddities(["abc", "def"]) == ['abc'])
print(oddities([123]) == [123])
print(oddities([]) == [])

print(odd_slicing([2, 3, 4, 5, 6]) == [2, 4, 6])
print(odd_slicing([1, 2, 3, 4]) == [1, 3])
print(odd_slicing(["abc", "def"]) == ['abc'])
print(odd_slicing([123]) == [123])
print(odd_slicing([]) == [])