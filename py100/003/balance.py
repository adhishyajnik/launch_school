# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 3: Variables

PRINCIPAL = 1000.00
INTEREST_RATE = 1.05

balance = PRINCIPAL * INTEREST_RATE**5
print('Principal: $' + str(PRINCIPAL))
print('Balance after 5 years at 5% interest: $' + str((int(balance*100))/100))
print('')
print('Year by year:')

balance = PRINCIPAL
balance *= INTEREST_RATE
print('Year 1: $' + str((int(balance*100))/100))

balance *= INTEREST_RATE
print('Year 2: $' + str((int(balance*100))/100))

balance *= INTEREST_RATE
print('Year 3: $' + str((int(balance*100))/100))

balance *= INTEREST_RATE
print('Year 4: $' + str((int(balance*100))/100))

balance *= INTEREST_RATE
print('Year 5: $' + str((int(balance*100))/100))