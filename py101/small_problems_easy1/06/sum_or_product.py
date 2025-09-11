def sum_cons(num):
    total = 0
    for number in range(num + 1):
        total += number
    return total

def mult_cons(num):
    total = 1
    for number in range(1, num + 1):
        total *= number
    return total

user_num = int(input('Please enter an integer greater than 0: '))
s_or_p = input('Enter "s" to compute the sum, '
               'or "p" to compute the product: ')

if s_or_p == 's':
    result = sum_cons(user_num)
    print(f'\nThe sum of the integers between 1 and {user_num} '
          f'is {result}.')
elif s_or_p == 'p':
    result = mult_cons(user_num)
    print(f'\nThe product of the integers between 1 and {user_num} '
          f'is {result}.')
else:
    print('Error: Unknown math operation.')