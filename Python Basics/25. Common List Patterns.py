basket = ['a', 'x', 't', 'b', 'c', 'z', 'y']
print('Example 1::')
basket.sort()
print(basket[::-1])     #Create a new list
print(basket)

print('Example 2::')
print(range(1,101))
print(list(range(1,101)))
print(list(range(101)))

print('Example 3::')
sentence = ' '
new_sentence = sentence.join(['Hello', 'Ayush', 'Prajapati'])
print(new_sentence)

print('Example 4::')
new_sentence2 = ' '.join(['Hello', 'Ayush', 'Prajapati'])
print(new_sentence2)

print('Example 5::')
friends = ['Ayush', 'Kohli', 'Anand', 'Dhoni', 'Rohit']
new_friend = ['Chahal']
friends.extend(new_friend)
friends.sort()
print(friends)