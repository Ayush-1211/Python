'''

    1. Instance Methods: The most common method type. Able to access data and properties unique to each instance.
    2. Static Methods: Cannot access anything else in the class. Totally self-contained code.
    3. Class Methods: Can access limited methods in the class. Can modify class specific details.

'''

class PlayerDetails:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(cls,num1,num2):       #cls is used to access parameters
        return num1 + num2

    @staticmethod
    def adding_things2(num3,num4):      # In staticmethod we do not have to use cls to access parameters
        return num3 + num4

print(PlayerDetails.adding_things(10,10))       #Using classmethod we do not have to Instantiate
print(PlayerDetails.adding_things2(30,30))