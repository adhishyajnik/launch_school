advice = "Few things in life are as important as house training your pet dinosaur."

# version 1
del_index = advice.find('house')
print(advice[:del_index])

# version 2
print(advice.split('house')[0])