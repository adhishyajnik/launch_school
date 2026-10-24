"""
Inputs: string
Outputs: integer or None

Explicit Rules:
- function accepts a series of space-separated commands as a string (a program)
- function runs commands left to right
- arithmetic operations pop the last element from the stack and perform the
  operation on the register value, and the register's new value is the result
  of the operation
- function should have the following command functionalities:

    - n: Place an integer value, n, in the register. Do not modify the stack.
    - PUSH : Push the current register value onto the stack. Leave the value in
      the register.
    - ADD : Pop a value from the stack and add it to the register value, storing
      the result in the register.
    - SUB : Pop a value from the stack and subtract it from the register value,
      storing the result in the register.
    - MULT : Pop a value from the stack and multiply it by the register value,
      storing the result in the register.
    - DIV : Pop a value from the stack and divide the register value by the
      popped stack value, storing the integer result back in the register.
    - REMAINDER : Pop a value from the stack and divide the register value by
      the popped stack value, storing the integer remainder of the division back
      in the register.
    - POP : Remove the topmost item from the stack and place it in the register.
    - PRINT : Print the register value.

- All operations are integer operations
- Assume all programs are valid and won't raise an error
- Initalize stack and register values to [] and 0 respectively

Data Structure/s:
- list
- integer
- string

Algorithm:
- initialize stack and register to [] and 0 respectively
- split the program into a list of strings/commands, program_list
- iterate through each command in program_list:
    - if the command can be converted to an integer:
        - set register to command converted to an integer
    - implement a match/case structure for the current command:
        - PUSH:
            - append register to stack
        - ADD:
            - set register to register + popped stack value
        - SUB:
            - set register to register - popped stack value
        - MULT:
            - set register to register * popped stack value
        - DIV:
            - set register to register // popped stack value
        - REMAINDER:
            - set register to register % popped stack value
        - POP:
            - set register to popped stack value
        - PRINT:
            - print register value
"""


def minilang(program):
    stack, register = [], 0
    program_list = program.split()
    for command in program_list:
        try:
            register = int(command)
        except ValueError:
            pass
        match command:
            case "PUSH":
                stack.append(register)
            case "ADD":
                register += stack.pop()
            case "SUB":
                register -= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "DIV":
                register = register // stack.pop()
            case "REMAINDER":
                register = register % stack.pop()
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)


minilang("PRINT")
# 0

minilang("5 PUSH 3 MULT PRINT")
# 15

minilang("5 PRINT PUSH 3 PRINT ADD PRINT")
# 5
# 3
# 8

minilang("5 PUSH POP PRINT")
# 5

minilang("3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT")
# 5
# 10
# 4
# 7

minilang("3 PUSH PUSH 7 DIV MULT PRINT")
# 6

minilang("4 PUSH PUSH 7 REMAINDER MULT PRINT")
# 12

minilang("-3 PUSH 5 SUB PRINT")
# 8

minilang("6 PUSH")
# (nothing is printed)
