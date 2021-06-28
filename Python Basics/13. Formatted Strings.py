print('Method 1::')
first_name = 'Ayush'
last_name = 'Prajapati'
age = 20
print('Hello ' + first_name + ' your last name is ' + last_name + ' and age is ' + str(age))

print('Method 2::')
# "f" is for formatted string
print(f'Hello {first_name} your last name is {last_name} and age is {age}')

print('Method 3::')
print('Hello {} your last name is {} and age is {}'.format(first_name,last_name,age))

print('Method 4::')
print('Hello {} your last name is {} and age is {}'.format('Ayush','Prajapati','20'))

print('Method 5::')
print('Hello {first_name} your last name is {last_name} and age is {age}'.format(first_name='Virat',last_name='Kohli',age='30'))

print('Method 6::')
print('Hello {0} your last name is {1} and age is {2}'.format(first_name,last_name,age))

