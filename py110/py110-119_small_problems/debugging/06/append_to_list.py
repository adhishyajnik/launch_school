def append_to_list_buggy(value, lst=[]):
    lst.append(value)
    return lst


print(append_to_list_buggy(1) == [1])
print(append_to_list_buggy(2) == [2])

"""
In Python, default parameters whose default value is mutable are shared between function calls.

Every time we invoke the function with a default value, the default value from prior invocations
is reused. Any mutations caused by the function will persist in the next function call.

To fix this, we can change the default value of lst to None, which is not mutable, and then
begin our function by creating an empty list if the value of the lst parameter is not None.
"""


def append_to_list(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)
    return lst


print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
