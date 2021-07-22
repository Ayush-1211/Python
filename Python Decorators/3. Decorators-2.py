def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func()

def hello():
    print('Hello!!!')

def bye():
    print('Byeee!!!')

hello2 = my_decorator(hello)
hello2

bye2 = my_decorator(bye)
bye2

# my_decorator(hello)()    [We can also write this]