# version 1
print(10 <= 42 <= 100)
print(10 <= 100 <= 100)
print(10 <= 101 <= 100)

# version 2
print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))