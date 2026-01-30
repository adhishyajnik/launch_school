"""
def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
"""

"""
When the sum function is defined as sum(numbers, factor)... it shadows the built-in sum function,
And when the sum function is invoked within that function, it raises an error for trying to
invoke the function from inside it.

We should rename the custom function something else, like multiply_sum
"""


def multiply_sum(numbers, factor):
    return factor * sum(numbers)


numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)
