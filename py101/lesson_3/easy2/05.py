numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# version 1 (might cause issues)
print(type(numbers) == list)
print(type(table) == list)

# version 2 (safer)
print(isinstance(numbers, list))
print(isinstance(table, list))