def leading_substrings(string_val):
    return [string_val[: idx + 1] for idx in range(len(string_val))]


def substrings(input_string):
    return [
        substring
        for idx in range(len(input_string))
        for substring in leading_substrings(input_string[idx:])
    ]


expected_result = [
    "a",
    "ab",
    "abc",
    "abcd",
    "abcde",
    "b",
    "bc",
    "bcd",
    "bcde",
    "c",
    "cd",
    "cde",
    "d",
    "de",
    "e",
]

print(substrings("abcde") == expected_result)  # True
