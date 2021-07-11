# Set is an unorder collection of unique values
my_set = {1,2,3,4,5,6,7,8,8,8}
print(my_set)
print('Example 1::')
my_set.add(100)
my_set.add(2)
print(my_set)

print('Example 2::')
my_list = [1,2,3,4,5,6,6,6]
print(set(my_list))

print('Example 3::')
print(5 in my_list)

print('Example 4::')
new_set = my_set.copy()
print(new_set)
my_set.clear()
print(my_set)