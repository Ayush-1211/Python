while True:
    try:
        age = int(input('Enter your age: '))
        10/age
        raise ValueError('Heyy cut it out!!!')
    except ZeroDivisionError:
        print('Please enter a number higher than 0!!!')
        continue
    else:
        print('Thank you!!!')
    finally:
        print('Okay, I am finally done!!')
    print('Can you hear me?')
    break