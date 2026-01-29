my_dict = {"p": 8, "q": 2, "r": 6}


def value_sort(pair):
    return pair[1]


def order_by_value(dct):
    sorted_pairs = sorted(dct.items(), key=value_sort)
    return [key for key, _ in sorted_pairs]


keys = ["q", "r", "p"]
print(order_by_value(my_dict) == keys)  # True
