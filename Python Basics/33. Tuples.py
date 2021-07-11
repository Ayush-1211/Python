# Tuples are immutable
my_tuple = (1,2,3,4,5,1,2,3,4,4,5)
print(my_tuple[1])
print(3 in my_tuple)
new_tuple = my_tuple[1:5]
print(new_tuple)
print(my_tuple.count(4))
print(my_tuple.index(3))

x,y,z, *other = (100,101,102,103,104,105,106)
print(x)
print(y)
print(z)
print(other)
