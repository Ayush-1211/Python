print('Example 1::')
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('Done with all the work!!')

print('Example 2::')
my_list = [1,2,3,4]
item = 0
while item<len(my_list):
    print(my_list[item])
    item += 1

print('Example 3::')
while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break