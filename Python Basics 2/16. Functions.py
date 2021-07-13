def show_msg():
    print('Hello Ayush!!')
show_msg()

print('Example 1:')
#parameters
def say_hello(name,age):
    print(f'Hello, {name} your age is {age}')
# positional arguments
say_hello('Ayush', 21)
say_hello('Kohli', 34)

print('Example 2:')
# keyword arguments
say_hello(name = 'Dhoni', age = 40)

print('Example 3:')
# Default parameters
def say_hii(name = 'Rohit', age = 35):
    print(f'Hii, {name} your age is {age}')
say_hii()
say_hii('Bhuvi')