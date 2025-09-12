def triangle(size):
    for num in range(1, size + 1):
        print(f'{' ' * (size - num)}{'*' * num}')

triangle(5)
triangle(9)