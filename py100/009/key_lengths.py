# Launch School - Introduction to Programming With Python
# Collections and Iteration, Chapter 9: Loops and Iterating

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

key_lengths = { name: len(name) for name in my_set if len(name) % 2 != 0 }
print(key_lengths)