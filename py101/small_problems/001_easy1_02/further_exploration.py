# Further Exploration: Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

# Default start and end parameter values of 1 and 99 (+ 1)
def odds_range(start = 1, end = 99):
    if start % 2 == 0:
        start += 1
    for number in range(start, end + 1, 2):
        print(number)

first = int(input('Input start number: '))
last = int(input('Input end number: '))

odds_range(first, last)