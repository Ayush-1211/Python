class Toy:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.my_dict = {
            'name' : 'Ayush',
            'age' : 21
        }
    def __str__(self):
        return f"{self.name}"
    def __len__(self):
        return 10
    def __call__(self):
        return ('Call!!')
    def __getitem__(self, i):
        return self.my_dict[i]
    def __del__(self):
        return 'Deleted!!'

action_figure = Toy('Car',0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure.__len__())
print(len(action_figure))
print(action_figure())
print(action_figure.__getitem__('name'))
print(action_figure.__del__())