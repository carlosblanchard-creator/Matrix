import json
import os

user_1 = {'id': 1, 'name': 'Carlos', 'age':30, 'city': 'Madrid'}
user_2 = {'id': 2, 'name': 'Juan', 'age':34, 'city': 'Barcelona'}


if os.path.exists('users.json') and os.path.getsize('users.json') > 0:
    with open('users.json', 'r') as f:
        users = json.load(f)
else:
    users = []

print(users)

users.append(user_1)
users.append(user_2)


print(users)

with open('users.json','w') as f:
    json.dump(users, f, indent=2)
    
print('Hola Mundo')










