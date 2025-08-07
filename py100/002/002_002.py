# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 2: Basic Operations

number = 4936
ones = number % 10
tens = ((number % 100) - ones) // 10
hundreds = ((number % 1000) - tens - ones) // 100
thousands = ((number % 10000) - hundreds - tens - ones) // 1000

print(number)
print('Ones place is     ', ones)
print('Tens place is     ', tens)
print('Hundreds place is ', hundreds)
print('Thousands place is', thousands)