'''
    Iterable-> list, tuple, string, set, dictionary
    Iterate-> one by one check each items in the collection
'''

user = {
    'name' : 'Ayush',
    'age' : 21,
    'can_swim' : True
}
print('Example 1::')
for item in user.items():
    print(item)

print('Example 2::')
for item in user.values():
    print(item)

print('Example 3::')
for item in user.keys():
    print(item)

print('Example 4::')
for item in user.items():
    key, value = item;
    print(key, value)

print('Example 5::')
for key,value in user.items():
    print(key,value)