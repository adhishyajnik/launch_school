"""
Inputs: minutes (integer)
Outputs: string

Explicit Rules:
- Function returns the 24-hour time in hh:mm format where 'minutes' is the number of minutes from midnight
- Negative 'minutes' is before midnight
- Positive 'minutes is after midnight
- May not use datetime module
- Must work with any integer input

Implicit Rules:
- inputting 0 returns "00:00"
- note that hours must be padded with a leading zero, and minutes must have 2 digits

Data Structure/s:
- input integer
- string output

Algorithm:
- set constant 'MINS_PER_HOUR' to 60
- set constant 'HOURS_PER_DAY' to 24
- set constant 'MINS_PER_DAY' to 'MINS_PER_HOUR' * 'HOURS_PER_DAY'
- if 'minutes' is less than 0, set 'minutes' to 'minutes' + 'MINS_PER_DAY'
    - repeat this until 'minutes' is non-negative
- if 'minutes' is greater than 'MINS_PER_DAY', set 'minutes' to 'minutes' - 'MINS_PER_DAY'
    - repeat this until 'minutes' is less than 'MINS_PER_DAY'
- get the integer quotient and remainder of 'minutes' and 'MINS_PER_HOUR', store it as a tuple 'hrs_mins'
- pad the start of both elements in 'hrs_mins' with zeroes until they're 2 digit strings
- concatenate the elements of hrs_mins with a colon in between, and return the result
"""

from datetime import datetime, timedelta

START_DATETIME = datetime(2025, 12, 14, 0, 0, 0)  # Midnight Sunday morning
MINS_PER_HOUR = 60
HOURS_PER_DAY = 24
MINS_PER_DAY = MINS_PER_HOUR * HOURS_PER_DAY


def time_of_day(minutes):
    while (minutes < 0) or (minutes > MINS_PER_DAY):
        minutes += MINS_PER_DAY if minutes < 0 else 0
        minutes -= MINS_PER_DAY if minutes > MINS_PER_DAY else 0
    hrs_mins = divmod(minutes, MINS_PER_HOUR)
    return f"{hrs_mins[0]:02d}:{hrs_mins[1]:02d}"


# FURTHER EXPLORATION
def day_and_time(minutes):
    duration = timedelta(0, 0, 0, 0, minutes)
    return datetime.strftime(START_DATETIME + duration, "%A %I:%M %p")


print(time_of_day(0) == "00:00")  # True
print(time_of_day(-3) == "23:57")  # True
print(time_of_day(35) == "00:35")  # True
print(time_of_day(-1437) == "00:03")  # True
print(time_of_day(3000) == "02:00")  # True
print(time_of_day(800) == "13:20")  # True
print(time_of_day(-4231) == "01:29")  # True

# FURTHER EXPLORATION TESTS
print(day_and_time(0) == "Sunday 12:00 AM")  # True
print(day_and_time(-3) == "Saturday 11:57 PM")  # True
print(day_and_time(35) == "Sunday 12:35 AM")  # True
print(day_and_time(-1437) == "Saturday 12:03 AM")  # True
print(day_and_time(3000) == "Tuesday 02:00 AM")  # True
print(day_and_time(800) == "Sunday 01:20 PM")  # True
print(day_and_time(-4231) == "Thursday 01:29 AM")  # True
