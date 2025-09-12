bill = float(input('What is the bill? '))
rate = float(input('What is the tip percentage? '))

tip = bill * rate * .01
total = bill + tip

print(f'\nThe tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')