"""
Inputs: int_list (list of integers)
Outputs: string

Explicit Rules:
- Function multiplies all integers in input list and divides the product by the number of list elements
- Function returns the result as a string with the value rounded to 3 decimal places

Implicit Rules:
- Input lists will have at least 2 integer elements
- Input lists will not have any non-integer elements
- All outputs include 3 significant figures (3 digits after the decimal place)s
    - 5 is displayed as "5.000"
    - 19.7 is displayed as "19.700"
    - 12456.56 is displayed as "12456.560"
    - 341.999 is displayed as "341.999"

Data Structure/s:
- input list
    - list elements are integers
- float quotient
- output string

Algorithm:
- initialize 'product' as 1
- iterate through each 'number' in 'int_list'
    - set 'product' to 'product' * 'number'
- initialize 'quotient' to 'product' divided by the length of 'int_list' (returns a float with at least 1 decimal place)
- round 'quotient' to 3 decimals, convert to a string, and pad the end with zeroes until it has 3 significant figures
- return the result

Sub-Algorithms:
Round 'quotient' to 3 decimals, convert to a string, and pad the end with zeroes until it has 3 significant figures
Input: float_num (float to round down), figures (number of sig figs to retain)
Output: string

Algorithm:
- initialize 'num_str' to 'float_num' rounded to 'sigfigs' places converted to a string
- initialize 'split_num' to 'num_str' split at the "." character
- if the length of 'split_num's second element is less than 'sigfigs', concatenate a "0" to the end of it
    - repeat this until the length of 'split_num's second element is equal to 'sigfigs'
- return 'split_num' joined with a "." character
"""


def sig_figs(float_num, figures):
    num_str = str(round(float_num, figures))
    split_num = num_str.split(".")
    while len(split_num[1]) < figures:
        split_num[1] += "0"
    return ".".join(split_num)


def multiplicative_average(int_list):
    product = 1
    for number in int_list:
        product *= number
    quotient = product / len(int_list)
    return sig_figs(quotient, 3)


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
