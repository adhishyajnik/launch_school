def leading_substrings(str2):
    return [str2[: idx + 1] for idx in range(len(str2))]


def substrings(str1):
    return [
        substring
        for idx in range(len(str1))
        for substring in leading_substrings(str1[idx:])
    ]


def is_palindrome(str3):
    return (str3 == str3[::-1]) and (len(str3) > 1)


def palindromes(str4):
    return [substring for substring in substrings(str4) if is_palindrome(substring)]


print(palindromes("abcd") == [])  # True
print(palindromes("madam") == ["madam", "ada"])  # True

print(
    palindromes("hello-madam-did-madam-goodbye")
    == [
        "ll",
        "-madam-",
        "-madam-did-madam-",
        "madam",
        "madam-did-madam",
        "ada",
        "adam-did-mada",
        "dam-did-mad",
        "am-did-ma",
        "m-did-m",
        "-did-",
        "did",
        "-madam-",
        "madam",
        "ada",
        "oo",
    ]
)  # True

print(
    palindromes("knitting cassettes")
    == [
        "nittin",
        "itti",
        "tt",
        "ss",
        "settes",
        "ette",
        "tt",
    ]
)  # True
