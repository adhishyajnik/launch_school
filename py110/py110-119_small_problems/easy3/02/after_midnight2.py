"""
Inputs: hhmm (string)
Outputs: integer

Explicit Rules:
- 'hhmm' is a string in the format HH:MM
- after_midnight returns the number of minutes after midnight
- before_midnight returns the number of minutes before midnight
- the return values should be in the range 0 - 1439

Implicit Rules:
- "00:00" and "24:00" return 0 for both functions

Data Structure/s:
- string
- list to split string at the ":"

Algorithms:
- set constant 'MINS_PER_HOUR' to 60
- set constant 'HOURS_PER_DAY' to 24
- set constant 'MINS_PER_DAY' to 'MINS_PER_HOUR' * 'HOURS_PER_DAY'

after_midnight:
    - initialize 'hrs_mins' as the result of splitting 'hhmm' at the ":" character
    - initialize 'mins' to the first element converted to an integer and multiplied by 'MINS_PER_HOUR'
    - set 'mins' to the sum of 'mins' and the second element converted to an integer
    - return the modulus of 'mins' and 'MINS_PER_DAY'

before midnight:
    - initialize 'hrs_mins' as the result of splitting 'hhmm' at the ":" character
    - initialize 'mins' to the first element converted to an integer and multiplied by 'MINS_PER_HOUR'
    - set 'mins' to 'MINS_PER_DAY' minus the sum of 'mins' and the second element converted to an integer
    - return the modulus of 'mins' and 'MINS_PER_DAY'

FURTHER EXPLORATION:
Rebuild the same function using Python's datetime.datetime class.

Algorithm:
- if the first two characters in 'hhmm' are "24" in that order, replace them with zeros
- initialize 'parsed' to the datetime module's string parse time method
    - the first argument is 'hhmm'
    - the second argument is a string with the strptime format codes for the 24-hour time formatted as HH:MM
- return the sum of the minute component of 'parsed' and (the product of its hour component and 'MINS_PER_HOUR')
"""

from datetime import datetime

MINS_PER_HOUR = 60
HOURS_PER_DAY = 24
MINS_PER_DAY = MINS_PER_HOUR * HOURS_PER_DAY


def after_midnight(hhmm):
    hrs_mins = hhmm.split(":")
    mins = int(hrs_mins[0]) * MINS_PER_HOUR
    mins = mins + int(hrs_mins[1])
    return mins % MINS_PER_DAY


def after_midnight2(hhmm):
    hrs, mins = [int(unit) for unit in hhmm.split(":")]
    return ((hrs * MINS_PER_HOUR) + mins) % MINS_PER_DAY


def before_midnight(hhmm):
    mins = MINS_PER_DAY - after_midnight2(hhmm)
    return mins % MINS_PER_DAY


# FURTHER EXPLORATION
def after_midnight3(hhmm):
    if hhmm.find("24") == 0:
        hhmm = "00" + hhmm[2:]
    parsed = datetime.strptime(hhmm, "%H:%M")
    return (parsed.hour * MINS_PER_HOUR) + parsed.minute


print(after_midnight("00:00") == 0)  # True
print(before_midnight("00:00") == 0)  # True
print(after_midnight("12:34") == 754)  # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)  # True
print(before_midnight("24:00") == 0)  # True

# FURTHER EXPLORATION TESTS
print(after_midnight3("00:00") == 0)  # True
print(before_midnight("00:00") == 0)  # True
print(after_midnight3("12:34") == 754)  # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight3("24:00") == 0)  # True
print(before_midnight("24:00") == 0)  # True
