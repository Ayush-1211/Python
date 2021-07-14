print('Example 1:')
def outer():
    x = 'local'
    def inner():
        x = 'nonlocal'
        print('Inner: ', x)
    inner()
    print('Outer: ', x)
outer()

print('Example 2:')
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('Inner: ', x)
    inner()
    print('Outer: ', x)
outer()