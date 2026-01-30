def unique_sequence(num_list):
    return [
        num for idx, num in enumerate(num_list) if idx == 0 or num != num_list[idx - 1]
    ]


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)  # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)  # True
