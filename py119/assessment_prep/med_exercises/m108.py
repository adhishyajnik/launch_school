"""
Algorithm:
- Define the base case: if nth is 1 or 2, return 1
- return the function called on the last term + the function called on the 2nd
  last term
"""


def fibonacci(nth):
    if nth <= 2:
        return 1
    return fibonacci(nth - 1) + fibonacci(nth - 2)


print(fibonacci(1) == 1)  # True
print(fibonacci(2) == 1)  # True
print(fibonacci(3) == 2)  # True
print(fibonacci(4) == 3)  # True
print(fibonacci(5) == 5)  # True
print(fibonacci(6) == 8)  # True
print(fibonacci(12) == 144)  # True
print(fibonacci(20) == 6765)  # True
