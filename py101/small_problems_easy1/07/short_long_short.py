def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    elif len(str1) > len(str2):
        return str2 + str1 + str2
    else:
        return 'Both strings are the same length.'

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")