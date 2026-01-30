"""
def get_key_value_buggy(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None


print(get_key_value_buggy({"a": 1}, "b"))
"""

"""
Line 2 will raise an KeyError if the key doesn't exist.

The more graceful way to check if a key exists and return its value in the same step is the dict.get() method
"""


def get_key_value(my_dict, key):
    return my_dict.get(key)


print(get_key_value({"a": 1}, "b"))
