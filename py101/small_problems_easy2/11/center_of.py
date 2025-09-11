def center_of(string):
    offset = 2 - len(string) % 2
    for num in range(offset):
        start = (len(string) // 2) - num
    return string[start:start + offset]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
print(center_of('') == '')                      # True