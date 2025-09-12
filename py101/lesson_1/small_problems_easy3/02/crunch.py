def crunch_1(string_):
    crunched = ''
    for idx in range(len(string_)):
        if idx + 1 < len(string_):
            if string_[idx] != string_[idx + 1]:
                crunched += string_[idx]
        else:
            crunched += string_[-1]
    return crunched

def crunch_2(string_):
    crunched = ''
    for idx in range(len(string_)):
        try:
            if string_[idx] != string_[idx + 1]:
                crunched += string_[idx]
        except:
            crunched += string_[-1]
    return crunched

def crunch(string_):
    crunched = ''
    for idx in range(len(string_)):
        if idx + 1 == len(string_) or string_[idx] != string_[idx + 1]:
            crunched += string_[idx]
    return crunched

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')