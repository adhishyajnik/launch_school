def leading_substrings(string_val):
    return [string_val[: idx + 1] for idx, _ in enumerate(string_val)]


def leading_substrings2(string_val):
    return [string_val[: idx + 1] for idx in range(len(string_val))]


# All of these examples should print True
print(leading_substrings("abc") == ["a", "ab", "abc"])
print(leading_substrings("a") == ["a"])
print(leading_substrings("xyzy") == ["x", "xy", "xyz", "xyzy"])
