# Launch School - Introduction to Programming With Python
# Collections and Iteration, Chapter 9: Loops and Iterating

def factorial(number):
    if type(number) is int:
        factorial = 1
        for factor in range(1, number+1):
            factorial *= factor
        return factorial
    else:
        return TypeError('TypeError: factorial argument must be of class \'int\'')

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(25))
print(factorial('Hello World!'))