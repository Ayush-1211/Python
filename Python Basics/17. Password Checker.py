username = input('Enter Your Username::')
password = input('Enter Your Password::')

password_length = len(password)
hidden_password = '*' * password_length

print(f'Hello {username}, your password, {hidden_password} is {password_length} letters long!!!')