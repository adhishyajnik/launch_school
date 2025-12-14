"""
Inputs: check_str (string)
Outputs: boolean

Explicit Rules:
- Function returns True if all parentheses in 'check_str' are properly closed, otherwise False
- Balanced pairs must start with a (, not a )

Implicit Rules:
- 'check_str' can contain no parentheses, in which case the function returns True
- The order of parentheses matters
    The string ")Hello World(" returns False

Data Structure/s:
- check_str string
- integer to count number of open parentheses

Algorithm:
- initialize 'count' to 0
- iterate through each 'char' in 'check_str'
    - if 'char' is '(' add 1 to 'count'
    - if 'char' is ')' subtract 1 from 'count'
    - return False if 'count' is ever negative
- if 'count' is positive, return True, otherwise return False

FURTHER EXPLORATION:
Expand the function's capabilities to take into account [], {}, '', and "" as well

Outputs: a string indicating which paired characters are not balanced

Algorithm:
- initialize constant 'OPENERS' to the string "([{'\""
- initialize constant 'CLOSERS' to the string ")]}'\""
- initialize 'unbalanced' to 0
- iterate through each 'char' in 'check_str'
    - if 'char' is in 'openers', increment 'unbalanced' by 1
    - if 'char' is in 'closers', decrement 'unbalanced' by 1
    - if 'unbalanced' is ever negative, return False
- return False if unbalanced is truthy, otherwise return True
"""

OPENERS = "([{'\""
CLOSERS = ")]}'\""


def is_balanced(check_str):
    unbalanced = 0
    for char in check_str:
        if char == "(":
            unbalanced += 1
        elif char == ")":
            unbalanced -= 1
        if unbalanced < 0:
            return False
    return False if unbalanced else True


# FURTHER EXPLORATION
def is_balanced2(check_str):
    unbalanced = 0
    for char in check_str:
        if char in OPENERS:
            unbalanced += 1
        elif char in CLOSERS:
            unbalanced -= 1
        if unbalanced < 0:
            return False
    return False if unbalanced else True


print(is_balanced("What (is) this?") == True)  # True
print(is_balanced("What is) this?") == False)  # True
print(is_balanced("What (is this?") == False)  # True
print(is_balanced("((What) (is this))?") == True)  # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)  # True
print(is_balanced(")Hey!(") == False)  # True
print(is_balanced("What ((is))) up(") == False)  # True

# FURTHER EXPLORATION TESTS
print(is_balanced2("(") == False)  # True
print(is_balanced2(")") == False)  # True
print(is_balanced2("[") == False)  # True
print(is_balanced2("]") == False)  # True
print(is_balanced2("{") == False)  # True
print(is_balanced2("}") == False)  # True
print(is_balanced2("'") == False)  # True
print(is_balanced2('"') == False)  # True
print(is_balanced2("") == True)  # True
