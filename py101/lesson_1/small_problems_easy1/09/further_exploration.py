GREGORYEAR = {
    'Spain': 1582,
    'Portugal': 1582,
    'France': 1582,
    'Poland': 1582,
    'Italy': 1582,
    'Luxembourg': 1582,
    'Denmark': 1700,
    'Norway': 1700,
    'Switzerland': 1700,
    'Great Britain': 1752,
    'Ireland': 1752,
    'Sweden': 1753,
    'Finland': 1753,
    'Japan': 1873,
    'Egypt': 1875,
    'Korea': 1896,
    'China': 1912,
    'Albania': 1912,
    'Latvia': 1915,
    'Lithuania': 1915,
    'Bulgaria': 1916,
    'Ukraine': 1918,
    'Russia': 1918,
    'Estonia': 1918,
    'Romania': 1919,
    'Yugoslavia': 1919,
    'Greece': 1923,
    'Turkey': 1926,
    'Saudi Arabia': 2016,
}

def is_leap_year(year):
    if year < adoption_year:
        return year % 4 == 0
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

adoption_year = 1752
country = input('What country are you from? ')
if country in GREGORYEAR:
    adoption_year = GREGORYEAR[country]

cur_year = int(input('Enter a year to check if it was a leap year in your country: '))
print(is_leap_year(cur_year))