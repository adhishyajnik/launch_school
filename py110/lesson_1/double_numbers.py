def double_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 1:
            result.append(num * 2)
        else:
            result.append(num)
    return result


def multiply_numbers(num_list, factor):
    result = [num * factor for num in num_list]
    return result


my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers))
print(my_numbers)

print(multiply_numbers(my_numbers, 5))
print(my_numbers)
