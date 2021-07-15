class PlayerDetails:
    def __init__(self,name,age):
        self.name = name    #attributes
        self.age = age
    def run(self):
        print('Run')

player1 = PlayerDetails('Ayush', 21)
player2 = PlayerDetails('Kohli', 34)
player2.attack = 50

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
player1.run()
player2.run()
print(player2.attack)