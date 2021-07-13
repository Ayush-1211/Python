print('Example 1:')
def sum(num1,num2):
    return num1 + num2
total = sum(10,10)
print(sum(15,total))
print(sum(15,sum(10,10)))

print('Example 2:')
def func(num1,num2):
    def another_func(n1,n2):
        return n1 + n2
    return another_func(num1,num2)
total = sum(10,20)
print(total)