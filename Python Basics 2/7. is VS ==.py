'''
    "==" compare value and data type
    "is" compare location
'''
print('Example 1::')
print(True == 1)        # True == bool(1)
print('' == 1)          # bool('') == 1
print([] == 1)          # bool([]) == 1
print(10 == 10.0)
print([] == [])
print([1,2,3] == [1,2,3])

print('Example 2::')
print(True is True)
print(1 is 1)
print([] == 1)
print(10 == 10)
print([] == [])
a = [1,2,3]
b = [1,2,3]
print(a is b)
