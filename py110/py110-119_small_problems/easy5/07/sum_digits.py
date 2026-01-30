def sum_digits2(integer):
    digits = list(str(integer))
    return sum([int(numstr) for numstr in digits])


def sum_digits(integer):
    return sum([int(digit) for digit in str(integer)])


print(sum_digits(23) == 5)  # True
print(sum_digits(496) == 19)  # True
print(sum_digits(123456789) == 45)  # True
