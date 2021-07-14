print('Example 1::')
def is_even(i):
    if i % 2 == 0:
        return True
    elif i % 2 != 0:
        return False
print(is_even(50))

print('Example 2::')
def is_even2(j):
    if j % 2 == 0:
        return True
    else:
        return False
print(is_even2(33))

print('Example 3::')
def is_even3(k):
    if k % 2 == 0:
        return True
    return False
print(is_even3(35))

print('Example 4::')        # Clean Code
def is_even4(l):
    return l % 2 == 0
print(is_even4(40))