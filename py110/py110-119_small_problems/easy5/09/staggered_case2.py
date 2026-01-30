def determine_case(character, index):
    return character.upper() if index % 2 == 0 else character.lower()


def staggered_case(str_val):
    result = ""
    upper = True
    for char in str_val:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char
    return result


string = "I Love Launch School!"
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = "ALL_CAPS"
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = "ignore 77 the 4444 numbers"
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case("") == "")  # True
