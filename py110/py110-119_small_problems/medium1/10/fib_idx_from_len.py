"""
As we've seen in the last few exercises, the Fibonacci series is a
computationally simple series. However, the results grow at an incredibly rapid
rate. For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 --
that's enormous, especially considering that it takes six iterations just to
find the first 2-digit Fibonacci number.

Write a function that calculates and returns the index of the first Fibonacci
number that has the number of digits specified by the argument. The first
Fibonacci number has an index of 1. You may assume that the argument is always
an integer greater than or equal to 2.

Since Python version 3.10.7, conversion of large integers to strings with more
than 4300 digits raises an error. This means that the last test case will raise
an error.

To bypass this limitation, we can use set sys.set_int_max_str_digits from the
sys module to a new upper limit. First, we import the sys module, then we call
sys.set_int_max_str_digits with the maximum digits desired for string
conversion:

    import sys

    sys.set_int_max_str_digits(50_000)

Inputs: int greater than or equal to 2
Outputs: int

Explicit Rules:
- Function must find the index of the first n-digit fibonacci number
    - e.g. find the index of the first 2-digit fibonacci number
    - e.g. find the index of the first 3-digit fibonacci number
- n passed to argument will always be an integer 2 or greater
- the first fibonacci number (1) has an index of 1
    - i.e. indexing of the fib sequence starts from 1 rather than 0

Implicit Rules:
- output will always be greater than or equal to 7, as the first 2-digit
  fibonacci number is the 7th one in the sequence (13)

Data Structure/s:
- int
- dict
- str

Algorithm:
- initialize idx to 1
- start a while True loop
    - calculate fibonacci(idx)
    - convert the result to a string and get its length
    - if the string length is equal to the digits argument
        - return idx
    - iterate idx by 1

sub-algorithm: fibonacci(idx)
    - reuse the memo-ized recursive fibonacci(nth) function
"""

import sys
import datetime as d


memo = {1: 1, 2: 1}


def fibonacci_memo(nth):
    if nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci_memo(nth - 1) + fibonacci_memo(nth - 2)
        return memo[nth]


def fibonacci(nth):
    prev_terms = [0, 1]
    for _ in range(nth - 1):
        prev_terms.append(prev_terms.pop(0) + prev_terms[0])
    return prev_terms.pop()


def find_fibonacci_index_by_length(digits):
    sys.set_int_max_str_digits(50_000)
    idx = 1
    while len(str(fibonacci_memo(idx))) < digits:
        idx += 1
    return idx


def find_fibonacci_index_by_length_1(digits):
    sys.set_int_max_str_digits(50_000)
    idx = 1
    while len(str(fibonacci(idx))) < digits:
        idx += 1
    return idx


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
s = d.datetime.now()
print(find_fibonacci_index_by_length(10000) == 47847)
e = d.datetime.now()
print(f"{(e - s).seconds}.{(e - s).microseconds} seconds")
print()
