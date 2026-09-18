"""
Write a function that implements a miniature stack-and-register-based
programming language that has the following commands (also called operations or
tokens):

    n: Place an integer value, n, in the register. Do not modify the stack.

    PUSH : Push the current register value onto the stack. Leave the value in
    the register.

    ADD : Pop a value from the stack and add it to the register value, storing
    the result in the register.

    SUB : Pop a value from the stack and subtract it from the register value,
    storing the result in the register.

    MULT : Pop a value from the stack and multiply it by the register value,
    storing the result in the register.

    DIV : Pop a value from the stack and divide the register value by the popped
    stack value, storing the integer result back in the register.

    REMAINDER : Pop a value from the stack and divide the register value by the
    popped stack value, storing the integer remainder of the division back in
    the register.

    POP : Remove the topmost item from the stack and place it in the register.

    PRINT : Print the register value.

All operations are integer operations (which is only important with DIV and
REMAINDER).

Programs will be supplied to your language function via a string argument. Your
function may assume that all arguments are valid programs -- i.e., they will not
do anything like trying to pop a non-existent value from the stack, and they
won't contain any unknown tokens.

Initialize the stack and register to the values [] and 0, respectively.


Inputs: str

Outputs: int

Explicit Rules:
- stack initalized to [] and register to 0
- all arithmetic operations begin by popping the topmost stack value,
  then performing the operation with the register value,
  then storing the result in the register
- SUB: register - popped stack value
- DIV: register / popped stack value, but return only the int portion
- REMAINDER: register % popped stack value
- POP: overwrites the current register value with the popped stack value
- PRINT: prints the register value
- n: overwrites the current register value
- PUSH: appends current register value to stack. Register value doesn't change.

Implicit Rules:
- function argument is a string of commands separated by spaces
- commands are executed from left to right, each one updating the register
  and stack values for the next command
- the function returns no value. if there are PRINT commands, values will be
  printed to the console.
- inputs and outsputs are always integers

Data Structure/s:
- str
- int
- list

Algorithm:
- initialize stack to [] and register to 0
- split the passed tokens string to token_list separated at every space
- loop through token_list and for each token:
    - set up a match/case for token where:
        - PUSH will append register to stack
        - ADD will pop from the stack, add that value to register,
        and assign the result to register
        - SUB will pop from the stack, subtract that value from register,
        and assign the result to register
        - MULT will pop from the stack, multiply that value by register,
        and assign the result to register
        - DIV will pop from the stack, divide that value by register,
        and assign the integer result to register
        - REMAINDER will pop from the stack, modulo that value by register,
        and assign the integer result to register
        - POP will pop from the stack and assign that value to register
        - PRINT will print register
        - wildcard case will coerce token to an integer
          and assign it to register
- return None
"""


def minilang(tokens):
    stack, register, token_list = [], 0, tokens.split()
    for token in token_list:
        match token:
            case "PUSH":
                stack.append(register)
            case "ADD":
                register += stack.pop()
            case "SUB":
                register -= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "DIV":
                register //= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _:
                register = int(token)
    return None


minilang("PRINT")
# 0

print()

minilang("5 PUSH 3 MULT PRINT")
# 15

print()

minilang("5 PRINT PUSH 3 PRINT ADD PRINT")
# 5
# 3
# 8

print()

minilang("5 PUSH POP PRINT")
# 5

print()

minilang("3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT")
# 5
# 10
# 4
# 7

print()

minilang("3 PUSH PUSH 7 DIV MULT PRINT")
# 6

print()

minilang("4 PUSH PUSH 7 REMAINDER MULT PRINT")
# 12

print()

minilang("-3 PUSH 5 SUB PRINT")
# 8

print()

minilang("6 PUSH")
# (nothing is printed)
