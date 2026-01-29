transactions = [
    {"id": 101, "movement": "in", "quantity": 5},
    {"id": 105, "movement": "in", "quantity": 10},
    {"id": 102, "movement": "out", "quantity": 17},
    {"id": 101, "movement": "in", "quantity": 12},
    {"id": 103, "movement": "out", "quantity": 20},
    {"id": 102, "movement": "out", "quantity": 15},
    {"id": 105, "movement": "in", "quantity": 25},
    {"id": 101, "movement": "out", "quantity": 18},
    {"id": 102, "movement": "in", "quantity": 22},
    {"id": 103, "movement": "out", "quantity": 15},
]


def transactions_for(item_num, transaction_list):
    return [
        transaction for transaction in transaction_list if transaction["id"] == item_num
    ]


def get_signed_val(item):
    return item["quantity"] if item["movement"] == "in" else -item["quantity"]


def is_item_available(item_num, transaction_list):
    quantities = [
        get_signed_val(transaction)
        for transaction in transactions_for(item_num, transaction_list)
    ]
    return sum(quantities) > 0


print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)  # True
