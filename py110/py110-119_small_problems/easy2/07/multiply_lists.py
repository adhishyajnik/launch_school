"""
Inputs: list1, list2 (two lists of numbers)
Outputs: list

Explicit Rules:
- Function returns a list where each element is the product of the same-indexed element of list1 and list2
- Arguments contain the same number of elements

Implicit Rules:
- Arguments only contain integer elements
- list1 and list2 are not empty

Data Structure/s:
- two input lists
- one output list
- zipped iterable

Algorithm:
- initialize 'output' to an empty list
- loop through each 'num_1' and 'num_2' in the zipped iterable of 'list1' and 'list2'
    - append the product of 'num_1' and 'num_2' to 'output'
- return 'output'
"""


def multiply_list(list1, list2):
    output = []
    for num1, num2 in zip(list1, list2):
        output.append(num1 * num2)
    return output


def multiply_list2(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
