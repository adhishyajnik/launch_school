"""
The Fibonacci series is a sequence of numbers in which each number is the sum of
the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third
number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth
is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:


F(1) = 1;
F(2) = 1;
F(n) = F(n - 1) + F(n - 2)    (where n > 2);


Write a function called fibonacci that computes the nth Fibonacci number, where
nth is an argument passed to the function.

If you're familiar with the concept of recursive functions, don't try to write a
recursive solution at this time; you'll do that in the next exercise. In other
words, write a procedural function that doesn't try to call itself.

If you don't know about or understand recursion, don't worry about it. You'll
learn soon enough.

Inputs: int
Outputs: int

Explicit Rules:
- Fibonacci sequence is a series of numbers starting with 1, 1, where the
  following numbers are the sum of the previous two numbers.
    - though technically you could think of the first term as 1
      and the 2nd term the sum of the first term and nothing.
- don't use recursive logic (i.e. don't pass a function to itself), use
  procedural logic (i.e. calculate each element?)

Implicit Rules:
- output will always be an integer
- if nth = 1 or 2, the output is 1
- input will always be a positive integer

Data Structure/s:
- int
- list / set

Algorithm:
- initialize prev_terms to [0, 1] which will hold the two previous elements
- loop a range the length of nth - 1:
    - pop index-0 element from prev_terms and add it to the remaining element
        and append the result to prev_terms
- return prev_terms[1]
"""


def fibonacci(nth):
    prev_terms = [0, 1]
    for _ in range(nth - 1):
        prev_terms.append(prev_terms.pop(0) + prev_terms[0])
    return prev_terms.pop()


print(fibonacci(1) == 1)  # True
print(fibonacci(2) == 1)  # True
print(fibonacci(3) == 2)  # True
print(fibonacci(4) == 3)  # True
print(fibonacci(5) == 5)  # True
print(fibonacci(6) == 8)  # True
print(fibonacci(12) == 144)  # True
print(fibonacci(20) == 6765)  # True
print(fibonacci(50) == 12586269025)  # True
print(fibonacci(75) == 2111485077978050)  # True
