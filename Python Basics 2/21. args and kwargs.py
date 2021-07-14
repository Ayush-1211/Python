# *args **kwargs

print('Example 1::')
def super_func(*args,**kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1=10, num2=10))

print('Example 2::')
# Rule: params, *args, default parameters, **kwargs
def super_func(name, *args, age='21', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    print(name,age)
    return sum(args) + total
print(super_func('Ayush', 1,2,3,4,5, num1=10, num2=10))

