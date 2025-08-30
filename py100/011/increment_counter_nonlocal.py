# Launch School - Introduction to Programming With Python
# Additional Topics, Chapter 11: More Stuff

def all_actions():
    counter = 0
    
    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)

    increment_counter()
    print(counter)

    increment_counter()
    print(counter)

    counter = 100
    increment_counter()
    print(counter)

all_actions()