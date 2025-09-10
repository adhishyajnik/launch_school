# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# Technically we don't need to test the absolute values; the result is the same whether positive or negative
def isnt_it_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

def i_i_o(num):
    return True if num % 2 == 1 else False

def abs_is_odd(num):
    return True if abs(num) % 2 == 1 else False

test_num = int(input('Enter a number to test each function: '))

print('\nisnt_it_odd() result:')
print(isnt_it_odd(test_num))

print('\ni_i_o() result:')
print(i_i_o(test_num))

print('\nabs_is_odd() result:')
print(abs_is_odd(test_num))