'''
    Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit.
'''

class PlayerDetails:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print('Run')
    def speak(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

player1 = PlayerDetails('Ayush',21)
player1.speak()