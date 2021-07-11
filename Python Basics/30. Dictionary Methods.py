print('Example 1::')
dictionary = {
    123 : [1,2,3],
    True : 'Ayush',
    'Hii' : 'Hello'
}
print(dictionary.get('Hii'))
print(dictionary.get('age', 21))

print('Example 2::')
dictionary2 = dict(name='Ayush Prajapati')
print(dictionary2)