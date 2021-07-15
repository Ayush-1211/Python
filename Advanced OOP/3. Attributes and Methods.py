class PlayerDetails:
    membership = True       # class object attribute (Static)
    def __init__(self,name,age):
        if self.membership:             # if PlayerDetails.membership:
            self.name = name    #attributes (Dynamic)
            self.age = age
        else:
            print('You are not member!!')
    def run(self):
        print(f'Your name is {self.name}')

player1 = PlayerDetails('Ayush', 21)
player2 = PlayerDetails('Kohli', 34)
player2.attack = 50

print(player1.membership)
player1.run()