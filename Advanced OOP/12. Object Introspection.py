'''
    Introspection is an ability to determine the type of an object at runtime.
'''

class User:
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('Logged In!!')
    def attack(self):
        print('Do nothing!!')

class Wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email)       # User.__init__(self,email)    we can also use this
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'{self.name} attacking with {self.power}% of power.')

wizard1 = Wizard('Ayush',89,'ayushprajapati1211@gmail.com')
print(dir(wizard1))         # Introspection
