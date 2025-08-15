# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 6: Flow Control

value = int(input('enter a number: '))

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _:                     # This is the default case
        print('value is neither 5 nor 6')