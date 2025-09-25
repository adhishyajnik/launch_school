ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

# version 1 (if no second dictionary)
ages['Marilyn'] = 22
ages['Spot'] = 237
print(ages)

# version 2 (if adding from second dictionary)
del(ages['Marilyn'], ages['Spot'])
additional_ages = {'Marilyn' : 22, 'Spot' : 237}
ages.update(additional_ages)
print(ages)