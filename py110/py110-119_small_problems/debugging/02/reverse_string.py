def reverse_string_buggy(string):
    for char in string:
        string = char + string

    return string


print(reverse_string_buggy("hello") == "olleh")

"""
The issue is that the for loop modifies the original string while iterating through it, so
on each iteration, the index being iterated over represents the same character it does in
the previous iteration.

We need to initialize an empty backwards string before the loop, and then reassign backwards to the result of char + backwards on each iteration.
"""


def reverse_string(string):
    backwards = ""
    for char in string:
        backwards = char + backwards

    return backwards


print(reverse_string("hello") == "olleh")
