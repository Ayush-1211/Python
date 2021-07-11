print('Example 1::')
dictionary = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(dictionary)
print(dictionary['a'])

print('Example 2::')
dictionary2 = {
    'a' : [1,2,3],
    'b' : 'ayush',
    'c' : True
}
print(dictionary2)
print(dictionary2['a'][1])

print('Example 3::')
my_list = [
    {
    'a' : 1,
    'b' : 2,
    'c' : 3
    },
    {
    'a' : [1,2,3],
    'b' : 'ayush',
    'c' : True
    }
]
print(my_list[1]['a'][2])