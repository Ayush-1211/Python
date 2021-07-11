my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,10}
print('Example 1::')
print(my_set.difference(your_set))

print('Example 2::')
my_set.discard(6)
print(my_set)

print('Example 3::')
my_set.difference_update(your_set)
print(my_set)

print('Example 4::')
my_set2 = {1,2,3,4,5,6}
your_set2 = {4,5,6,7,8,9,10}
print(my_set2.intersection(your_set2))
print(my_set2 & your_set2)

print('Example 5::')
print(my_set2.isdisjoint(your_set2))

print('Example 6::')
print(my_set2.union(your_set2))
print(my_set2 | your_set2)

print('Example 7::')
my_set3 = {4,5}
your_set3 = {4,5,6,7,8,9,10}
print(my_set3.issubset(your_set3))
print(your_set3.issubset(my_set3))

print('Example 8::')
print(my_set3.issuperset(your_set3))
print(your_set3.issuperset(my_set3))

print('Example 9::')
# Find out who missed the class
school = {'Bobby','Tammy','Jammy','Sally','Danny'}      #School Database
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']  #Attendance 
print(school.difference(attendance_list))