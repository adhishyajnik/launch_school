"""
Inputs: Integer
Outputs: Intger

Explicit Rules:
- Function returns the nth fibonacci number where n is the passed integer
- Fibonacci sequence starts with 1, 1, and then all subsequent numbers are the
  sum of the previous two numbers
- Don't write a recursive function. Write a procedural function.

Implicit Rules:
- Function will only be passed valid positive integers

Data Structure/s:
- Integer

Algorithm:
- if nth is 1 or 2, return 1
- else fib_prev = 1, fib_cur = 1
- iterate through each _ in a range starting at 2 and ending at nth
    - fib_new = fib_cur + fib_prev
    - fib_prev = fib_cur
    - fib_cur = fib_new
- return fib_cur
"""


def fibonacci(nth):
    if nth == 1:
        return 1
    fib_prev, fib_cur = 0, 1
    for _ in range(1, nth):
        nth_fib = fib_cur + fib_prev
        fib_cur, fib_prev = nth_fib, fib_cur
    return nth_fib


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
