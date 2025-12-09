'''
Input: number of available blocks (integer)
Output: leftover blocks after building tallest possible structure (integer)

Explicit rules:
    - Building blocks are cubes
    - Structure is built in layers
    - The top layer is a single block
    - A block in an upper layer must be supported by 4 blocks
    - A block in a lower layer can support more than 1 block
    - You cannot leave gaps between blocks
Implicit rules:
    - There may be cases where all blocks are usable -- should clarify this
    - The structure is a pyramid -- should clarify this
        - the top layer is a single block,
        - the next layer is 4 blocks arranged in a grid
        - the next layer has 9 blocks arranged in a grid
    - the number of blocks in each layer is the square of the layer number, numbered top down

Further notes/questions:
    - There are indeed cases where there all blocks are usable; passing 5 to the function returns 0
    - Based on the test cases, it seems like our pyramid theory is correct - we can't add more blocks than needed to support the layer above
    - We can get an input of 0 blocks as well, which returns 0
    - A 1-layer tower uses 1 block

Data Structure/s:
    - We can use a range to square consecutive integers
    - We could build the tower as a nested list if necessary

Algorithm:
1. Set layer number to 1
2. Set remaining blocks to the number of available blocks
2. Subtract the square of the layer number from the remaining blocks
3. If the result is 0, return 0 remaining blocks
4. If the result is negative, return the number of remaining blocks
5. If the result is positive, increment layer number by 1
6. Repeat steps 2-5 until a value has been returned
'''

def calculate_leftover_blocks(available_blocks):
    current_layer = 1
    while True:
        leftover_blocks = available_blocks - (current_layer**2)
        if leftover_blocks == 0:
            return leftover_blocks
        elif leftover_blocks < 0:
            return available_blocks
        current_layer += 1
        available_blocks = leftover_blocks

# Test cases
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True