my_list = ['a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'g']

duplicates = []
for values in my_list:
    if my_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)