"""
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.

Inputs: dictionary
Outputs: dictionary

Explicit Rules:
- input_dict has unique keys and values
- function returns dictionary where input_dict's keys and values and its values are keys

Implicit Rules:
- The order of pairs in the returned dictionary should be in the same order as input_dict

Data Structure/s:
- Dictionary

Algorithm:
- perform a dictionary comprehension on input_dict
    that returns the value as the key, and the key as the value
    iterating over each key and value input_dict's items
"""


def invert_dict(dict):
    return {value: key for key, value in dict.items()}


print(
    invert_dict(
        {
            "apple": "fruit",
            "broccoli": "vegetable",
            "salmon": "fish",
        }
    )
    == {
        "fruit": "apple",
        "vegetable": "broccoli",
        "fish": "salmon",
    }
)  # True
