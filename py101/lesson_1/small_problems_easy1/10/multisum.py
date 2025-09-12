def multisum(num):
    sum_list = [ number for number in range(1, num+1) if number % 3 == 0 or number % 5 == 0 ]
    return sum(sum_list)

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)