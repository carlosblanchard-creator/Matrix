import json
import os
Users_File = 'users.json'

#Acceso a ficheros JSON
def load_users():
    if os.path.exists(Users_File):
        with open(Users_File,'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []
        return users
    return []

def save_users(users):
    with open(Users_File,'w') as f:
        json.dump(users, f, indent=2)


#Funciones de Usuario
def create_user(name, age, city):
    users = load_users()
    new_id = max([i['id'] for i in users]) + 1 if users else 1
    new_user = {"id": new_id, "name": name, "age": age, "city": city}
    users.append(new_user)

    save_users(users)
    
    print(f"New user, {new_user['name']}, added successfully with ID {new_user['id']}")
    return new_user

def get_user(get_id):
    users = load_users()
    for u in users:
        if u['id']==get_id:
            return u
    return None

def delete_user(delete_id):
    users = load_users()
    users_f = [u for u in users if u['id']!=delete_id]
    if len(users) == len(users_f):
        print(f"User ID {delete_id} was not found")
        return False
    else:
        save_users(users_f)
        print(f"User ID {delete_id} was deleted successfully")
        return True
    



create_user('Alberto', 86, 'Sevilla')
delete_user(3)
delete_user(4)