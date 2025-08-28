# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 9: Loops and Iterating

age = 22
# print('You are ' + str(age) + ' years old.')

# years_in_future = range(10, 41, 10)
for incr in range(0, 41, 10):
    new_age = age + incr
    if new_age == age:
        print(f'You are {age} years old.')
        continue
    print(f'In {incr} years, you will be {new_age} years old.')

# age += 10
# print('In ' + str(years_in_future[0]) + ' years, you will be ' + str(age) + ' years old.')

# age += 10
# print('In ' + str(years_in_future[1]) + ' years, you will be ' + str(age) + ' years old.')

# age += 10
# print('In ' + str(years_in_future[2]) + ' years, you will be ' + str(age) + ' years old.')

# age += 10
# print('In ' + str(years_in_future[3]) + ' years, you will be ' + str(age) + ' years old.')