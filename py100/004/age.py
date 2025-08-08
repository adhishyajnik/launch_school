# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 4: Input/Output

CURRENT_AGE = input('How old are you? ')
INTERVAL = range(10, 41, 10)
projected_age = int(CURRENT_AGE)

print()
print(f'You are {CURRENT_AGE} years old now.')

projected_age += INTERVAL[0]
print(f'In {INTERVAL[0]} years, you will be {projected_age} years old.')

projected_age += INTERVAL[0]
print(f'In {INTERVAL[1]} years, you will be {projected_age} years old.')

projected_age += INTERVAL[0]
print(f'In {INTERVAL[2]} years, you will be {projected_age} years old.')

projected_age += INTERVAL[0]
print(f'In {INTERVAL[3]} years, you will be {projected_age} years old.')