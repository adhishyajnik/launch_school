"""
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

Inputs: dictionary, list
Outputs: dictionary

Explicit Rules:
- input_list contains some or all keys from input_dict
- function returns a new dictionary containing only the key-value pairs where the keys are in input_list

Implicit Rules:
- order of pairs in returned dictionary should match order of pairs in input_dict

Data Structure/s:
- dictionary
- list
- dictionary comprehension

Algorithm:
- perform a dictionary comprehension that returns the key and value
    iterating over input_dict's items
    if the key is in input_list
"""


def keep_keys(dict, keys):
    return {key: value for key, value in dict.items() if key in keys}


input_dict = {
    "red": 1,
    "green": 2,
    "blue": 3,
    "yellow": 4,
}

keys = ["red", "blue"]
expected_dict = {"red": 1, "blue": 3}
print(keep_keys(input_dict, keys) == expected_dict)  # True
