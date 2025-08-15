# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 5: Functions and Methods

def multiply(a, b):
    return a * b

number_1 = input('Enter the first number: ')
number_2 = input('Enter the second number: ')

product = multiply(float(number_1), float(number_2))

print(f'{number_1} * {number_2} = {product}')