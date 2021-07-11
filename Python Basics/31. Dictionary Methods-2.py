print('Example 1::')
dictionary = {
    'basket' : [1,2,3],
    'name' : 'Ayush',
    'Hii' : 'Hello'
}
print('basket' in dictionary)
print('age' in dictionary)

print('Example 2::')
print('basket' in dictionary.keys())
print('Ayush' in dictionary.values())
print(dictionary.items())

print('Example 3::')
print(dictionary.clear())
print(dictionary)

print('Example 4::')
new_dictionary = {
    'basket' : [1,2,3],
    'name' : 'Ayush',
    'Hii' : 'Hello'
}
dictionary2 = new_dictionary.copy()
print(new_dictionary)
print(dictionary2)

print('Example 5::')
new_dictionary = {
    'basket' : [1,2,3],
    'name' : 'Ayush',
    'Hii' : 'Hello'
}
dictionary2 = new_dictionary.copy()
print(new_dictionary.clear())
print(dictionary2)

print('Example 6::')
user = {
    'name' : 'Ayush',
    'age' : 21,
    'hobby' : 'Reading'
}
print(user.pop('hobby'))
print(user)

print('Example 7::')
user2 = {
    'name' : 'Ayush',
    'age' : 21,
    'hobby' : 'Reading'
}
print(user2.popitem())      #Remove item randomly
print(user2)

print('Example 8::')
user3 = {
    'name' : 'Ayush',
    'age' : 21,
    'hobby' : 'Reading'
}
user3.update({'age':20})
print(user3)