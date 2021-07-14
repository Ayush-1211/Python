print('Example 1:')
total = 0
def count():
    global total
    total += 1
    return total
count()
count()
print(count())

print('Example 2:')
total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total))))