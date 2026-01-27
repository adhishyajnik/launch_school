# Practice Problems

# Sorting

# 1. Sort the following list of numbers first in ascending numeric order,
# then in descending numeric order. Do not mutate the list.
"""
lst = [10, 9, -6, 11, 7, -16, 50, 8]

ascending = sorted(lst)
descending = sorted(lst, reverse=True)

print(lst)
print(ascending)
print(descending)
"""

# 2. Repeat the previous exercise but, this time, perform the sort by
# mutating the original list.
"""
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
"""

# 3. Repeat problem 2 but, this time, sort the list as string values. Both
# the list passed to the sorting function and the returned list should
# contain numbers, not strings.
"""
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst)

lst.sort(reverse=True, key=str)
print(lst)
"""

# 4. How would you sort the following list of dictionaries based on the year
# of publication of each book, from the earliest to the most recent?
"""
books = [
    {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "published": "1967",
    },
    {
        "title": "The Book of Kells",
        "author": "Multiple Authors",
        "published": "800",
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "published": "1869",
    },
]


def published(dict_obj):
    return int(dict_obj["published"])


books.sort(key=published)
print(books)
"""

# Nested Data Structures

# 1. For each object shown below, demonstrate how you would access the
# letter g.
"""
lst1 = ["a", "b", ["c", ["d", "e", "f", "g"]]]
print(lst1[2][1][3])

lst2 = [
    {"first": ["a", "b", "c"], "second": ["d", "e", "f"]},
    {"third": ["g", "h", "i"]},
]
print(lst2[1]["third"][0])

lst3 = [["abc"], ["def"], {"third": ["ghi"]}]
print(lst3[2]["third"][0][0])

dict1 = {"a": ["d", "e"], "b": ["f", "g"], "c": ["h", "i"]}
print(dict1["b"][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {"1st": {"d": 3}, "2nd": {"e": 2, "f": 1}, "3rd": {"g": 0}}
print(list(dict2["3rd"].keys())[0])
"""

# 2. For each of these collection objects, demonstrate how you would change
# the value 3 to 4.
"""
lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1)

lst2 = [{"a": 1}, {"b": 2, "c": [7, 6, 5], "d": 4}, 3]
lst2[2] = 4
print(lst2)

dict1 = {"first": [1, 2, [3]]}
dict1["first"][2][0] = 4
print(dict1)

dict2 = {"a": {"a": ["1", "two", 3], "b": 4}, "b": 5}
dict2["a"]["a"][2] = 4
print(dict2)
"""

# 3. Given the following code, what will the final values of a and b be? Try
# to answer without running the code.
"""
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# The final value of a is 2 and the final value of b is [3, 8]
print(a)
print(b)
"""

# 4. One of the most frequently used real-world string operations is that of
# "string substitution," where we take a hard-coded string and modify it with
# various parameters from our program.

# Given the object shown below, print the name, age, and gender of each
# family member:
"""
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

for name in munsters:
    age = munsters[name]["age"]
    gender = munsters[name]["gender"]
    print(f"{name} is a {age}-year-old {gender}.")
"""

# Comprehensions

# 1. For the following dictionary, compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

# Expected reult:
# 444
"""
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

male_ages = [
    munsters[person]["age"]
    for person in munsters
    if munsters[person]["gender"] == "male"
]
print(sum(male_ages))
"""

# 2. Given the following data structure, return a new list with the same
# structure, but with the values in each sublist ordered in ascending order.
# Use a comprehension if you can. (Try using a for loop first.)

# The string values should be sorted as strings, while the numeric values
# should be sorted as numbers.

# Expected result:
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
"""
lst = [["b", "c", "a"], [2, 11, -3], ["blue", "black", "green"]]

sorted_lst = [sorted(sublist) for sublist in lst]
print(sorted_lst)
"""

# 3. Given the following data structure, return a new list with the same
# structure, but with the values in each sublist ordered in ascending order
# as strings (that is, the numbers should be treated as strings). Use a
# comprehension if you can. (Try using a for loop first.)

# Expected result:
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
"""
lst = [["b", "c", "a"], [2, 11, -3], ["blue", "black", "green"]]

str_sorted_lst = [sorted(sublist, key=str) for sublist in lst]
print(str_sorted_lst)
"""

# 4. Given the following data structure, write some code that uses
# comprehensions to define a dictionary where the key is the first item in
# each sublist, and the value is the second.

# Expected result:
#   {
#       'a': 1,
#       'b': 'two',
#       'sea': {'c': 3},
#       'D': ['a', 'b', 'c']
#   }
"""
lst = [["a", 1], ["b", "two"], ["sea", {"c": 3}], ["D", ["a", "b", "c"]]]

lst_dict = {sublist[0]: sublist[1] for sublist in lst}
print(lst_dict)
"""

# 5. Given the following data structure, sort the list so that the sub-lists
# are ordered based on the sum of the odd numbers that they contain. You
# shouldn't mutate the original list.

# Expected result:
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
"""
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]


def odd_sum_key(numlist):
    return sum([num for num in numlist if num % 2 != 0])


odd_sum_sorted = sorted(lst, key=odd_sum_key)
print(odd_sum_sorted)
"""

# 6. Given the following data structure, return a new list identical in
# structure to the original but, with each number incremented by 1. Do not
# modify the original data structure. Use a comprehension.

# Expected result:
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
"""
lst = [{"a": 1}, {"b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}]


def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}


incremented = [increment_values(subdict) for subdict in lst]
print(incremented)
"""

# 7. Given the following data structure return a new list identical in
# structure to the original, but containing only the numbers that are
# multiples of 3.

# Expected result:
# [[], [3, 12], [9], [15, 18]]
"""
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


def keep_mult_3(list_elem):
    return [num for num in list_elem if num % 3 == 0]


mult3 = [keep_mult_3(sublist) for sublist in lst]
print(mult3)
"""

# 8. Given the following data structure, write some code to return a list that
# contains the colors of the fruits and the sizes of the vegetables. The sizes
# should be uppercase, and the colors should be capitalized.

# Expected result:
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
"""
dict1 = {
    "grape": {
        "type": "fruit",
        "colors": ["red", "green"],
        "size": "small",
    },
    "carrot": {
        "type": "vegetable",
        "colors": ["orange"],
        "size": "medium",
    },
    "apricot": {
        "type": "fruit",
        "colors": ["orange"],
        "size": "medium",
    },
    "marrow": {
        "type": "vegetable",
        "colors": ["green"],
        "size": "large",
    },
}


def colors_or_sizes(attr_dict):
    if attr_dict["type"] == "fruit":
        return [color.capitalize() for color in attr_dict["colors"]]
    else:
        return attr_dict["size"].upper()


colors_and_sizes = [colors_or_sizes(attributes) for attributes in dict1.values()]
print(colors_and_sizes)
"""

# 9. Given the following data structure, write some code to return a list that
# contains only the dictionaries where all the numbers are even.

# This problem may prove challenging. Try it, but don't stress about it. If
# you don't solve it in 20 minutes, you can look at the answer.

# Expected result:
# [{'e': [8], 'f': [6, 10]}]
"""
lst = [
    {"a": [1, 2, 3]},
    {"b": [2, 4, 6], "c": [3, 6], "d": [4]},
    {"e": [8], "f": [6, 10]},
]


def contains_evens_only(dictionary):
    for numlist in dictionary.values():
        for num in numlist:
            if num % 2 != 0:
                return False
            else:
                continue
    return True


def contains_evens_only2(dictionary):
    for numlist in dictionary.values():
        are_even = [num % 2 == 0 for num in numlist]
        if not all(are_even):
            return False
        else:
            continue
    return True


def contains_evens_only3(dictionary):
    are_even = [num % 2 == 0 for numlist in dictionary.values() for num in numlist]
    return all(are_even)


result1 = [subdict for subdict in lst if contains_evens_only3(subdict)]
print(result1)

result2 = [
    subdict
    for subdict in lst
    if all([num % 2 == 0 for numlist in subdict.values() for num in numlist])
]
print(result2)
"""

# 10. A UUID (Universally Unique Identifier) is a type of identifier often
# used to uniquely identify items, even when some of those items were created
# on a different server or by a different application. That is, without any
# synchronization, two or more computer systems can create new items and label
# them with a UUID with no significant risk of stepping on each other's toes.
# It accomplishes this feat through massive randomization. The number of
# possible UUID values is approximately 3.4 X 10E38, which is a huge number.
# The chance of a conflict, a "collision", is vanishingly small with such a
# large number of possible values.

# Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the
# letters a-f) represented as a string. The value is typically broken into 5
# sections in an 8-4-4-4-12 pattern,
# e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

# Note that our description of UUIDs is a simplified description of how UUIDs
# are formed. There are several UUID versions, each with some non-random
# characteristics in some of the bits. These different versions can play a
# part in certain applications.

# Write a function that takes no arguments and returns a string that contains a UUID.
"""
import random

SECTIONS = [8, 4, 4, 4, 12]
HEX_CHARS = "abcdefg1234567890"


def get_rand_char():
    return HEX_CHARS[random.randint(0, 16)]


def get_rand_string(sect_len):
    return "".join([get_rand_char() for _ in range(sect_len)])


def generate_UUID():
    return "-".join([get_rand_string(sect) for sect in SECTIONS])


new_UUID = generate_UUID()
print(new_UUID)
"""

# 11. The following dictionary has list values that contains strings. Write
# some code to create a list of every vowel (a, e, i, o, u) that appears in
# the contained strings, then print it.

# Start by trying to write this using nested loops.

# Extra Challenge: Once your nested loop code works, try to refactor the code
# so it uses a single list comprehension. (You can print the resulting list
# outside of the comprehension.)
"""
VOWELS = "aeiou"

dict1 = {
    "first": ["the", "quick"],
    "second": ["brown", "fox"],
    "third": ["jumped"],
    "fourth": ["over", "the", "lazy", "dog"],
}

list_of_vowels = [
    char
    for lst in dict1.values()
    for string in lst
    for char in string
    if char in VOWELS
]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
"""
