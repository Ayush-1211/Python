def highest_even(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)
print(highest_even([2,10,8,6,4,23,11,7,98,44]))