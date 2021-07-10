print('Adding Methods::')
print('Example 1::')
basket = [100, 101, 102, 103, 104, 105]
new_list = basket.append(106)
print(basket)
print(new_list)

print('Example 2::')
basket.append(107)
new_list = basket
print(basket)
print(new_list)

print('Example 3::')
new_list = basket.insert(0,99)
print(basket)

print('Example 4::')
new_list = basket.extend([108,109])
print(basket,"\n")

print('Removing Methods::')
print('Example 1::')
basket.pop()
print(basket)

print('Example 2::')
basket.pop(3)   #index number
print(basket)

print('Example 3::')
basket.remove(105)      #index value
print(basket)

print('Example 4::')
new_list = basket.remove(104)
print(new_list)

print('Example 5::')
new_list = basket.pop(2)
print(new_list)

print('Example 6::')
new_list = basket.clear()
print(new_list)
print(basket)
