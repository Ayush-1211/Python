import random

print(random.random())
print(random.choice([1,2,3,4,5]))
print(random.randint(1,100))

my_list  = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)
