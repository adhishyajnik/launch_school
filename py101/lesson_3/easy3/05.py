my_color = 'purple'

# version 1
def is_color_valid(color):
    return color == "blue" or color == "green"

# version 2
def is_color_valid2(color):
    return color in ["blue", "green"]

print(is_color_valid(my_color))
print(is_color_valid2(my_color))