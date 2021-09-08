from random import randint

answer = randint(1,10)

while True:
    try:
        guess = int(input(f'Guess a number:  '))
        if  0 < guess < 11:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey User, I said 1~10')
    except ValueError:
        print('Please enter a number')
        continue