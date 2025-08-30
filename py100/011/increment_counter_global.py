# Launch School - Introduction to Programming With Python
# Additional Topics, Chapter 11: More Stuff

counter = 0

def increment_counter():
    global counter
    counter += 1

print(counter)

increment_counter()
print(counter)

increment_counter()
print(counter)

counter = 100
increment_counter()
print(counter)