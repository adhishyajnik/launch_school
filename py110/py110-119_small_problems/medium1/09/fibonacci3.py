"""
Our recursive fibonacci function from the previous exercise isn't very
efficient. It starts slowing down with an nth argument value somewhere around
35-60, depending on your system. One way to improve the performance of our
recursive fibonacci function (and other recursive functions) is to use
memoization.

Memoization is an approach that involves saving a computed answer for future
reuse, instead of computing it from scratch every time it is needed. In the case
of our recursive fibonacci function, using memoization saves calls to
fibonacci(nth - 2) because the necessary values have already been computed by
the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci
function to use memoization.

Hint: One approach to memoization is to use a lookup table, such as an object,
for storing and accessing previously computed values.

Explicit Rules: - on this version of the fibonacci function, use memoization to
store the nth - 2 value so that it can be reused quickly on the next iteration
as nth - 1, thus speeding up the recursive function.

Implicit Rules: - nth - 2 on iteration x is equal to nth - 1 on iteration x + 1
- the function call should have a way of storing a new nth - 2 each time it's
  called

Data Structure/s:
- int
- list or dict

Algorithm:
- initialize memo to an empty dict before the function definition
- start the function
    - if nth is 1 or 2:
        - return 1
    - else if nth is one of the keys in memo:
        - return its associated value
    - else:
        - assign fibonacci(nth - 1) + fibonacci(nth - 2) to nth key in memo
        - return the value associated with the nth key in memo

fibonacci(1)
returns 1

fibonacci(2)
returns 1

fibonacci(3)
memo[3] = fibonacci(3 - 1) + fibonacci(3 - 2)
          fibonacci(2) + fibonacci(1)
          1 + 1
          2
          memo = {3: 2}
return memo[3] --> 2

fibonacci(4)
memo[4] = fibonacci(4 - 1) + fibonacci(4 - 2)
          fibonacci(3) + fibonacci(2)
          fibonacci(3) + 1
            memo[3] = fibonacci(3 - 1) + fibonacci(3 - 2)     + 1
            fibonacci(2) + fibonacci(1)                       + 1
            1 + 1                                             + 1
            2                                                 + 1
            memo = {3: 2}
            return memo[3] --> 2                              + 1
          2 + 1
return memo[4] --> 3

fibonacci(5)
memo[5] = fibonacci(5 - 1) + fibonacci(5 - 2)
          fibonacci(4) + fibonacci(3)
            memo[4] = fibonacci(4 - 1) + fibonacci(4 - 2)               + fib(3)
            fibonacci(3) + fibonacci(2)                                 + fib(3)
            fibonacci(3) + 1                                            + fib(3)
              memo[3] = fibonacci(3 - 1) + fibonacci(3 - 2)       + 1   + fib(3)
              fibonacci(2) + fibonacci(1)                         + 1   + fib(3)
              1 + 1                                               + 1   + fib(3)
              2                                                   + 1   + fib(3)
              memo = {3: 2}
              return memo[3] --> 2                                + 1   + fib(3)
            2 + 1                                                       + fib(3)
            3 + fibonacci(3)
              3 in memo:
              return memo[3]                                            + 3
              2                                                         + 3
              2 + 3
              5
          memo = {3: 2, 4: 5}
return memo[4] --> 3
"""

import datetime as d

memo = {1: 1, 2: 1}


def fibonacci(nth):
    if nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]


print(fibonacci(1) == 1)  # True
print(fibonacci(2) == 1)  # True
print(fibonacci(3) == 2)  # True
print(fibonacci(4) == 3)  # True
print(fibonacci(5) == 5)  # True
print(fibonacci(6) == 8)  # True
print(fibonacci(12) == 144)  # True
print(fibonacci(20) == 6765)  # True


print()

for n in range(1, 101):
    s = d.datetime.now()
    print(f"Term {n}: {fibonacci(n)}")
    e = d.datetime.now()
    print(f"{(e - s).seconds}.{(e - s).microseconds} seconds")
    print()
