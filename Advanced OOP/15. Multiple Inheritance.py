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
    def check_arrows(self):
        print(f'{self.arrows} Arrows left.')
    def run(self):
        print('Run!!')

class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hybrid1 = Hybrid('Ayush', 90, 100)
hybrid1.run()
hybrid1.sign_in()
hybrid1.attack()
hybrid1.check_arrows()