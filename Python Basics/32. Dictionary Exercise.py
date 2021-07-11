user = {
     'age': 21,
     'username': 'Ayush',
     'weapons': ['AK-47', 'AK-56'],
     'is_active': True,
     'clan': 'India'
}
print(user.keys())
user['weapons'].append('Short gun')
print(user)
user.update({'is_banned':False})
print(user)
user['is_banned'] = True
print(user)
user2 = user.copy()
user2.update({'age':20,'username':'Ayush_1211'})
print(user2)