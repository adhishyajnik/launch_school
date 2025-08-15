# Launch School - Introduction to Programming With Python
# Introduction to Programming, Chapter 7: Intro To Collections

my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

print(my_list == another_list)
print(my_list is another_list)
print(my_list[3] == another_list[3])
print(my_list[3] is another_list[3])