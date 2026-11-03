"""
Inputs: list of integers
Outputs: integer

Explicit Rules:
- Function returns an integer such that if it's summed with the integers in
  input_list, it returns the first prime number greater than the sum of
  input_list alone
- input_list will always contain 2 or more integers
- the returned integer must be positive
- input_list may contain repeated integers

Implicit Rules:
- prime numbers are numbers greater than 1 whose only factors are themselves and
  1

Data Structure/s:
- list
- int

Algorithm:
- set input_sum to the sum of the integers in input_list
- set next_int to 1
- start a while True loop:
    - set current_sum to input_sum + next_int
    - if current_sum % 2 is 0 (it's even, not prime):
        - increment next_int by 1
        - continue
    - if current_sum is greater than 5 and its last digit is 5 (not prime):
        - increment next_int by 1
        - continue
    - set factors to 0
    - iterate through each factor in a range from 1 to (current_sum // 2) + 1, with a
      step of 2 (skip even numbers):
        - if current_sum % factor is 0 and factor is not 1:
            - increment factors by 1
    - if factors is 0:
        - return next_int
    - else:
        - increment next_int by 1
"""


def nearest_prime_sum(input_list):
    input_sum = sum(input_list)
    next_int = 1
    while True:
        current_sum = input_sum + next_int
        if current_sum % 2 == 0:
            next_int += 1
            continue
        if current_sum > 5 and str(current_sum)[-1] == "5":
            next_int += 1
            continue
        factors = 0
        for factor in range(1, (current_sum // 2) + 1, 2):
            if current_sum % factor == 0 and factor != 1:
                factors += 1
        if factors == 0:
            return next_int
        else:
            next_int += 1


print(nearest_prime_sum([1, 2, 3]) == 1)  # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)  # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)  # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5)  # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
