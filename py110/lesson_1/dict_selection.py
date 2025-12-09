def select_fruit(items_dictionary):
    result = {}
    for item in items_dictionary:
        if items_dictionary[item] == "Fruit":
            result[item] = items_dictionary[item]
    return result


def select_fruit_2(items_dictionary):
    result = {
        item: items_dictionary[item]
        for item in items_dictionary
        if items_dictionary[item] == "Fruit"
    }
    return result


def select_fruit_3(items_dictionary, selection_criterion):
    result = {
        item: value
        for item, value in items_dictionary.items()
        if value == selection_criterion
    }
    return result


produce = {
    "apple": "Fruit",
    "carrot": "Vegetable",
    "pear": "Fruit",
    "broccoli": "Vegetable",
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }
print(select_fruit_2(produce))  # { apple: 'Fruit', pear: 'Fruit' }
print(select_fruit_3(produce, "Fruit"))  # { apple: 'Fruit', pear: 'Fruit' }
