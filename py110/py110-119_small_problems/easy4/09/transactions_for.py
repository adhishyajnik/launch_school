"""
Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list containing only the transactions for the specified inventory item.

Inputs: integer, list
Outputs: list

Explicit Rules:
- return only the dictionary objects from input_list where the dictionary's "id" value is input_id
"""

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


print(
    transactions_for(101, transactions)
    == [
        {"id": 101, "movement": "in", "quantity": 5},
        {"id": 101, "movement": "in", "quantity": 12},
        {"id": 101, "movement": "out", "quantity": 18},
    ]
)  # True
