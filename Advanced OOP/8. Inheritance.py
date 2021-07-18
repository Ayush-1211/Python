class User:
    def sign_in(self):
        print('Logged In!!')

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'{self.name} attacking with {self.power}% of power.')

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows
    def attack(self):
        print(f'{self.name} attacking with Arrows and {self.arrows} arrows left.')

wizard1 = Wizard('Ayush',89)
archer1 = Archer('Kohli',20)
wizard1.attack()
archer1.attack()

print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,User))
print(isinstance(wizard1,object))