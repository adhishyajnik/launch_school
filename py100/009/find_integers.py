# Launch School - Introduction to Programming With Python
# Collections and Iteration, Chapter 9: Loops and Iterating

def find_integers(hetero_list):
    return [ elem for elem in hetero_list if type(elem) is int ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)
print(integers)