'''
    A function is called pure function if it always returns the same result for same argument values and
    it has no side effects like modifying an argument (or global variable) or outputting something.
    The only result of calling a pure function is the return value.
'''

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list
print(multiply_by2([1,2,3]))