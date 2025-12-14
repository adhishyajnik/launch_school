"""
Inputs: name (string)
Outputs: string

Explicit Rules:
- 'name' is a string with a first name, a space, and a last name
- Function returns a string with the last name, a comma and a space, and then the first name
- The names only include 2 elements (no middle name/initial, no prefix or suffix, etc.)

Implicit Rules:
- Case from the input is preserved in the output

Data Structures:
- name string
- names list
- output string

Algorithm:
- initialize 'names' to a list where 'name' is split at the space character
- initialize 'flipped' to a slice of 'names' with a -1 step to reverse it
- use the string ", " to join the elements of 'flipped' and return the result

FURTHER EXPLORATION
Refactor the current solution so it can accommodate this. The middle names should be listed after the first name.

Algorithm:
- initialize 'names' to a list where 'name' is split at the space character
- initialize 'first' to a string containing all but the last element of 'names', joined with a space
- concatenate the last element of 'names' with a comma, a space, and 'first' and then return the result
"""


def swap_name_orig(name):
    return ", ".join(name.split()[::-1])


def swap_name(name):
    names = name.split()
    first = " ".join(names[: len(names) - 1])
    return names[-1] + ", " + first


print(swap_name("Joe Roberts") == "Roberts, Joe")  # True
print(
    swap_name("Karl Oskar Henriksson Ragvals") == "Ragvals, Karl Oskar Henriksson"
)  # True
