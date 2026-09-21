"""
In the previous exercise, we developed a procedural solution for computing the
nth Fibonacci number.

This sequence can also be computed using a recursive function. A recursive
function is one in which the function calls itself. For example, the following
function is a recursive function that computes the sum of all integers between 1
and n:


def sum_recursive(n):
    if n == 1:
        return 1

    return n + sum_recursive(n - 1)


A recursive function has three primary qualities:

    1. It must have a base case. This is a condition that tells the function to
       stop recursing and begin the process of returning to the first call to
       the function. This is often the simplest case - the condition for which
       you already know the answer. In sum_recursive, the base case occurs when
       n == 1. At this point, we know the answer: sum_recursive(1) == 1. Thus,
       we can return the value 1.

    2. The function must call itself except when handling the base case.

    3. Each recursive call must be "closer" to the base case than the current
       call. For instance, in sum_recursive(3), we call sum_recursive(2), which
       is closer to the base case. Likewise, sum_recursive(2) subsequently calls
       sum_recursive(1), which is the base case.

You may recall from the revious exercise that the Fibonacci sequence follows a
simple set of rules:


F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)


If you study this set of rules, you can see that the algorithm is defined
recursively:

    1. The base case occurs when the argument is 1 or 2; both of these arguments
       result in a value of 1.

    2. The Fibonacci function calls itself. In fact, it calls itself twice.

    3. Except when dealing with the base case, each call to the Fibonacci
       function comes closer to the base case. In this case, both F(n - 1) and
       F(n - 2) are closer to the base case than F(n).

Given this recursive algorithm, try to write a recursive function that computes
the nth Fibonacci number, where nth is an argument passed to the function.

Inputs: int
Outputs: int

Explicit Rules:
- must use a recursive function
- function returns the nth term in the fibonacci sequence

Implicit Rules:
- nth will always be a positive integer
- output will always be a positive integer

Data Structure/s:
- int
- list?

Algorithm:
- define the base case: if nth is 1 or 2, return 1
- return fibonacci(nth - 1) + fibonacci(nth - 2)

if nth == 1:
satisfies base case, return 1

if nth == 2:
satisfied base case, return 1

if nth == 3:
doesn't satisfy base case
fibonacci(2) + fibonacci(1) --> 1 + 1 = 2

if nth == 4:
doesn't satisfy base case
fibonacci(3) + fibonacci(2) --> fibonacci(3) + 1 --> 2 + 1 = 3
    fibonacci(3)
    doesn't satisfy base case
    fibonacci(2) + fibonacci(1) --> 2
"""

import datetime as d


def fibonacci(nth):
    if nth < 3:
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


print()

for n in range(1, 41):
    s = d.datetime.now()
    print(f"Term {n}: {fibonacci(n)}")
    e = d.datetime.now()
    print(f"{(e - s).seconds}.{(e - s).microseconds} seconds")
    print()
