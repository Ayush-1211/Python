print('Example 1::')
for i,char in enumerate('Ayush'):
    print(i,char)

print('Example 2::')
for i,char in enumerate([0,1,2,3]):
    print(i,char)

print('Example 3::')
for i,char in enumerate((0,1,2,3)):
    print(i,char)

print('Example 4::')
for i,char in enumerate(list(range(100))):
    if char==50:
        print(f'Index number is:: {i}')