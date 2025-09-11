def evensies(list_):
    out_list = []
    for idx in range(len(list_)):
        if idx % 2 == 1:
            out_list.append(list_[idx])
    return out_list

print(evensies([2, 3, 4, 5, 6]))
print(evensies([1, 2, 3, 4]))
print(evensies(["abc", "def"]))
print(evensies([123]))
print(evensies([]))