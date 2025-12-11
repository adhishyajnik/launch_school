"""
Inputs: floating point number
Outputs: string

Explicit Rules:
- function takes a floating point number representing a 0-360 degree angle
- function returns string representation of the angle in degrees, minutes, seconds
- use the degree symbol ('\u00b0') to represent degrees
- use a single quote for minutes, and double quote symbol for seconds.
- There are 60 seconds in a minute and 60 minutes in a degree

Implicit Rules:
- Passing 0 to the function returns "0°00'00\""
- Passing 360 to the function returns "360°00'00\"" or "0°00'00\""
- Minutes and Seconds must have 2 digits

Data Structure/s:
- input float
- output string

Algorithm:
- initialize 'degrees_float' to the modulo of 'input_float' and 360
- initialize 'degrees' to the integer-coerced 'degrees_float'
- initialize 'minutes_float' to ('degrees_float' minus 'degrees') * 60
- initialize 'minutes' to the integer-coerced 'minutes_float'
- initialize 'seconds_float' to ('minutes_float' - 'minutes') * 60
- initialize 'seconds' to the integer-coerced 'seconds_float'
- pad 'minutes' with leading zeroes to make it a 2-digit string
- pad 'seconds' with leading zeroes to make it a 2-digit string
- create an f-string combining 'degrees', 'minutes', 'seconds', and their respective symbols

Sub-algorithms:
Pad a number with zeroes to make it an n-length string
Inputs: integer/string (value), integer (length), pad character (pad_char)
Outputs: string

- if the length of 'value' is greater than 'length', return 'value' coerced to a string
- initialize 'output' to (pad_char * 'length') + 'value'
- calculate the difference in length between 'output' and 'length', set the result to 'diff'
- return the slice of 'output' from index 'diff' to the end
"""

DEGREE = "\u00b0"
MINUTE = "'"
SECOND = '"'

MINS_PER_DEG = 60
SECS_PER_MIN = 60


def pad_start(value, length, pad_char):
    if len(str(value)) > length:
        return str(value)
    output = (str(pad_char) * length) + str(value)
    diff = len(output) - length
    return output[diff:]


def get_normalized_angle(float_angle):
    sign = -1 if float_angle < 0 else 1
    float_angle = sign * (abs(float_angle) % 360)
    return float_angle


def dms(float_angle, normalized=False):
    if normalized:
        flt_val = get_normalized_angle(float_angle)
    else:
        flt_val = float_angle % 360

    int_val = int(flt_val)

    dms_string = f"{int_val}{DEGREE}"
    unit = MINUTE
    factor = MINS_PER_DEG

    flt_val = abs(flt_val)
    int_val = abs(int_val)

    for _ in range(2):
        flt_val = (flt_val - int_val) * factor
        int_val = int(flt_val)
        str_val = pad_start(int_val, 2, 0)

        dms_string += str_val + unit
        unit = SECOND
        factor = SECS_PER_MIN

    return dms_string


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))  # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420))  # 300°00'00"

print(dms(59.8765, True))
print(dms(-47, True))
print(dms(0, True))
print(dms(-587, True))
print(dms(5000.3453, True))

print(dms(59.8765))
print(dms(-47))
print(dms(0))
print(dms(-587))
print(dms(5000.3453))
