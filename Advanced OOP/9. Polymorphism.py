'''
    Polymorphism: Polymorphism lets us define methods in the child class that have the same name as
                  the methods in the parent class.
                  In inheritance, the child class inherits the methods from the parent class.
'''

class User:
    def sign_in(self):
        print('Logged In!!')
    def attack(self):
        print('Do nothing!!')

class Wizard(User):
    def __init__(self,name,power):
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

wizard1 = Wizard('Ayush',89)
archer1 = Archer('Kohli',20)

print('Example 1:')
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

print('Example 2:')
for char in [wizard1,archer1]:
    char.attack()

print('Example 3:')
wizard1.attack()