'''
    A generator-function is defined like a normal function, but whenever it needs to generate a value,
    it does so with the yield keyword rather than return
'''

def generator_function(num):
    for i in range(num):
        yield i*2

g = generator_function(20)
next(g)
next(g)
next(g)
print(next(g))