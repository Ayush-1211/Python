my_set = {char for char in 'Hello'}
my_set2 = {num for num in range(0,10)}
my_set3 = {num**2 for num in range(0,10)}
my_set4 = {num**2 for num in range(0,10) if num % 2 == 0}

print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)