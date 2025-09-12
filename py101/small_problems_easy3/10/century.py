def lnd(number, digits):
    return number % (10**digits)

def f2d(number):
    return number // 100

def tens(number):
    return (number // 10) % 10

def century(year):
    suffixes = ('th', 'st', 'nd', 'rd')
    eras = ('BCE', 'CE')
    cent = f2d(abs(year)) + (lnd(abs(year), 2) > 0)
    if lnd(cent, 1) < 4 and tens(cent) != 1:
        return f'{cent}{suffixes[lnd(cent, 1)]} {eras[year > 0]}'
    else:
        return f'{cent}{suffixes[0]} {eras[year > 0]}'

def century_verbose(year):
    suffixes = ('th', 'st', 'nd', 'rd')
    eras = ('BCE', 'CE')
    cent = (abs(year) // 100) + ((abs(year) % 100) > 0)
    if (cent % 10) < 4 and (cent // 10 % 10) != 1:
        return f'{cent}{suffixes[cent % 10]} {eras[year > 0]}'
    else:
        return f'{cent}{suffixes[0]} {eras[year > 0]}'

print(century(2000))
print(century(2001))
print(century(1965))
print(century(256))
print(century(5))
print(century(10103))
print(century(1052))
print(century(1127))
print(century(11201))
print(century(0))
print(century(-553))
print(century(-1965))