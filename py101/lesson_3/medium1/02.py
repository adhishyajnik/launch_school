def factors(number):
    divisor = number
    result = []
    while divisor > 0:                          # change != to > so negative numbers don't run the while block
        if number % divisor == 0:               # checks that number divides by divisor without a remainder
            result.append(number // divisor)
        divisor -= 1
    return result