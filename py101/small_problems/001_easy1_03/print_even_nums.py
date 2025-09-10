# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# Iterating over all numbers
def evens_from_all_nums():
    for number in range(1, 100):
        if number % 2 == 0:
            print(number)

# Iterating over evens only; have to start from 2 instead of 1
def evens_from_even_nums():
    for number in range(2, 100, 2):
        print(number)

evens_from_even_nums()