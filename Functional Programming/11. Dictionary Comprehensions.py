simple_dict = {
    'a' : 1,
    'b' : 2
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)