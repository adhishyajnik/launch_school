# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# Iterating over all numbers:
def odds_from_all_nums():
    for number in range(1, 100):
        if number % 2 == 1:
            print(number)

# Iterating over odds only:
def odds_from_odd_nums():
    for number in range(1, 100, 2):
        print(number)

choice = input('Input 1 to run odds_from_all_nums(), or 2 to run odds_from_odd_nums(): ')

if choice == '1':
    odds_from_all_nums()
else:
    odds_from_odd_nums()