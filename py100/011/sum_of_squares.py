# Launch School - Introduction to Programming With Python
# Additional Topics, Chapter 11: More Stuff

def sum_of_squares(num1, num2):
    def square(num1):
        return num1 * num1
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))
print(sum_of_squares(5, 12))