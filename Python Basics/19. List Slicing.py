print('Example 1::')
amazon_cart = ['iPhone', 'Notebook', 'Watch', 'Pen', 'Grapes']
print(amazon_cart[0:2])

print('Example 2::')
print(amazon_cart[0::2])

print('Example 3::')
amazon_cart[0] = 'MacBook'
print(amazon_cart)          #Strings are immutable but Lists are mutable

print('Example 4::')
new_cart = amazon_cart[0:]
new_cart[0] = 'Gum'
print(new_cart)
print(amazon_cart)

print('Example 5::')
new_cart = amazon_cart
new_cart[0] = 'Gum'
print(new_cart)
print(amazon_cart)

print('Example 6::')
amazon_cart2 = ['Mobile', 'TV', 'Watch', 'Bicycle', 'Toys', 'Vegetables']
new_cart = amazon_cart2[:]
new_cart[0] = 'Gum'
print(new_cart)
print(amazon_cart2)