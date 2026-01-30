def staggered_case(str_val):
    result = ""
    for idx, char in enumerate(str_val.lower()):
        result += char.upper() if idx % 2 == 0 else char.lower()
    return result


string = "I Love Launch School!"
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = "ALL_CAPS"
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = "ignore 77 the 4444 numbers"
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case("") == "")  # True
