# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 9: Loops and Iterating

names = [
    'Chris',
    'Max',
    'Karis',
    'Victor',
]
upper_names = []
# index = 0

# while index < len(names):
#     upper_name = names[index].upper()
#     upper_names.append(upper_name)
#     index += 1

for elem in names:
    upper_name = elem.upper()
    upper_names.append(upper_name)

print(upper_names)