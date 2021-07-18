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

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows
    def attack(self):
        print(f'{self.name} attacking with Arrows and {self.arrows} arrows left.')

wizard1 = Wizard('Ayush',89,'ayushprajapati1211@gmail.com')
archer1 = Archer('Kohli',20)

print(wizard1.email)