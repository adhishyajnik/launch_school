def sum_of_sums(num_list):
    sequences = [num_list[: idx + 1] for idx in range(len(num_list))]
    return sum([sum(seq) for seq in sequences])


print(sum_of_sums([3, 5, 2]) == 21)  # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)  # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)  # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)  # True
