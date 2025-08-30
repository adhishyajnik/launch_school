# Launch School - Introduction to Programming With Python
# Collections and Iteration, Chapter 9: Loops and Iterating

import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break