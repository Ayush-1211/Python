basket = ['a', 'x', 't', 'b', 'c', 'z', 'y']
print('Example 1::')
basket.sort()
print(basket)

print('Example 2::')
basket2 = ['y', 'x', 't', 'b', 'c', 'z', 'a']
print(sorted(basket2))      #sorted does not change actual basket values
print(basket2)

print('Example 3::')
basket3 = ['b', 'x', 't', 'a', 'c', 'z', 'y']
new_basket = basket3[:]
new_basket.sort()
print(new_basket)
print(basket3)

print('Example 4::')
basket4 = ['z', 'x', 't', 'a', 'c', 'b', 'y']
new_basket2 = basket4.copy()
new_basket2.sort()
print(new_basket2)
print(basket4)

print('Example 5::')
basket4.reverse()
print(basket4)