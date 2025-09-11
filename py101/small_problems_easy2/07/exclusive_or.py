def xor(value1, value2):
    if (value1 or value2) and (not (value1 and value2)):
        return True
    return False

print(xor(5, 0))
print(xor(False, True))
print(xor(1, 1))
print(xor(True, True))