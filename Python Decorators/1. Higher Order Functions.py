'''
    A function is called Higher Order Function if it contains other functions as a parameter or
    returns a function as an output
'''

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(10))