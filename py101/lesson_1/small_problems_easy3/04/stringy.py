def stringy1(num):
    mult = num // 2
    if num % 2 == 0:
        return '10' * mult
    else:
        return ('10' * mult) + '1'

def stringy(size):
    result = ''
    for num in range(size):
        digit = '1' if num % 2 == 0 else '0'
        result += digit
    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True