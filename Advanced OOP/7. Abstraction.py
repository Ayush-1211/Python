'''
    Abstraction: Abstraction is used to hide the internal functionality of the function from the users.
                 The users only interact with the basic implementation of the function, but inner working is hidden.
'''

# In python there is no any PRIVATE and PUBLIC method like Java. So, It's not totally secure.

class PlayerDetails:
    def __init__(self,name,age):
        self._name = name       # _name means it should be private so don't try to change it.
        self._age = age
    def run(self):
        print('Run')
    def speak(self):
        print(f'Hello, my name is {self._name} and I am {self._age} years old.')

player1 = PlayerDetails('Ayush',21)
player1.speak()
