print('Example 1:')
def multiply_by2(item):
    return item * 2
print(list(map(multiply_by2, [1,2,3])))

print('Example 2:')
my_list = [1,2,3]
def multiply_by3(item):
    return item * 3
print(list(map(multiply_by3, my_list)))
print(my_list)