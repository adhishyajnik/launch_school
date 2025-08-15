# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 6: Flow Control

def all_caps(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

user_string = input('Enter a string. If it\'s longer than\n10 characters, I\'ll capitalize it: ')
print(all_caps(user_string))