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
conversion.


Inputs: integer Outputs: integer

Explicit Rules:
- Function is passed an integer representing a number of digits
- Function returns the index of the first fibonacci number that is has the
  passed number of digits
- The first fibonacci number is index 1
- Argument will always be an integer greater than or equal to 2 (digits)
- Use sys.set_int_max_str_digits() to 50,000

Data Structure/s:
- integer
- maybe string to get number of digits

Algorithm:
- set index to 1
- Start a While True loop:
    - convert the result of fibonacci(index) to a string
    - if the string length is equal to digits
        return index
    - increment index by 1
"""

import sys

sys.set_int_max_str_digits(50000)

memo = {}


def fibonacci(nth):
    if nth <= 2:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]


def find_fibonacci_index_by_length(digits):
    index = 1
    while True:
        if len(str(fibonacci(index))) == digits:
            return index
        index += 1


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
