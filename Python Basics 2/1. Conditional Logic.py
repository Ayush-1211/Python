is_old = True
is_licenced = True

if is_old and is_licenced:
    print('You are old enough to drive, and you have driving licence!')
elif is_old:
    print('Your are old enough to drive!')
elif is_licenced:
    print('You have your licence so you can drive now!')
else:
    print('You cannot drive!')
print('Done!!!')