"""
Inputs: string of integers
Outputs: integer

Explicit Rules:
- function returns the greatest product of 4 consecutive integers in the
  input string
- the argument will always have more than 4 digits

Implicit Rules:

Data Structure/s:
- string
- int
- list

Algorithm:
- set products to an empty list
- set num_products to the length of input_string minus 3
- iterate through each start_idx in a range ending at num_products
    - set product to 1
    - iterate through each idx in a range starting at start_idx and ending at
      start_idx + 4:
        - set product to product * int(input_string[idx])
    - append product to products
- return the maximum value in products
"""


def greatest_product(input_string):
    products = []
    num_products = len(input_string) - 3
    for start_idx in range(num_products):
        product = 1
        for idx in range(start_idx, start_idx + 4):
            product *= int(input_string[idx])
        products.append(product)
    return max(products)


print(greatest_product("23456") == 360)  # 3 * 4 * 5 * 6
print(greatest_product("3145926") == 540)  # 5 * 9 * 2 * 6
print(greatest_product("1828172") == 128)  # 1 * 8 * 2 * 8
print(greatest_product("123987654") == 3024)  # 9 * 8 * 7 * 6
