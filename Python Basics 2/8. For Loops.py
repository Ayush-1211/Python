print('Example 1::')
for name in 'Ayush':
    print(name)

print('Example 2::')
for items in [1,2,3,4]:
    print(items)

print('Example 3::')
for items in (1,2,3,4):
    print(items)

print('Example 3::')
for items in {1,2,3,4}:
    print(items)

print('Example 4::')
for items in (1,2,3,4):
    for value in ['a','b','c','d']:
        print(items,value)