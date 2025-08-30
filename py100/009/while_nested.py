# Launch School - Introduction to Programming With Python
# Collections and Iteration, Chapter 9: Loops and Iterating

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index_outer = 0

while index_outer < len(my_list):
    nested_list = my_list[index_outer]
    index_inner = 0
    while index_inner < len(nested_list):
        elem = nested_list[index_inner]
        if elem % 2 == 0:
            print(elem)
        index_inner += 1
    index_outer += 1