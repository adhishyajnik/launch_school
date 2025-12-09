"""
Inputs: 6 numbers (integers)
Outputs: String

Explicit Rules:
- User is prompted for each integer separately
- Program prints a message if the last integer is among the first 5
- Duplicates within the first five integers do not matter
- Each prompt text is unique:
    - Enter the 1st number:
    - Enter the 2nd number:
    - Enter the 3rd number:
    - Enter the 4th number:
    - Enter the last number:
- The output string is one of two formats:
    - [last_number] is in [number1],[number2],[number3],[number4],[number5].
    - [last_number] isn't in [number1],[number2],[number3],[number4],[number5].

Questions:
- Are negative numbers allowed?
    - Based on test cases, no negative numbers will be input

Data Structures:
- Because the output string prints the inputs in order, we must use a list to store inputs 1-5
- We can store the inputs as their native strings and compare them against each other as such

Algorithm:
- Prompt the user for the first five numbers and add each to a list 'first_five'
- Prompt the user for the sixth number, 'last'
- Join the all the numbers from 'first_five' into single a string separated by commas 'first_five_string'
- If 'last' is in 'first_five', print 'last' is in 'first_five_string'
- Otherwise, print 'last' isn't in 'first_five_string'
"""

first_five = []

first_five.append(input("Enter the 1st number: "))
first_five.append(input("Enter the 2nd number: "))
first_five.append(input("Enter the 3rd number: "))
first_five.append(input("Enter the 4th number: "))
first_five.append(input("Enter the 5th number: "))

last = input("Enter the last number: ")

first_five_string = ",".join(first_five)

if last in first_five:
    print(f"{last} is in {first_five_string}.")
else:
    print(f"{last} isn't in {first_five_string}.")
