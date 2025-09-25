a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
# prints True because Python uses interning on short strings
# and integers to allow different identifiers assigned the
# same value to reference the same object in memory

# to be more specific, Python pre-assigns memory locations
# for all integers from -5 to 256, so any variables with
# the same value in that range will be interned together