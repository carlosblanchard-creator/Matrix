from JSON_functions import load_file, save_file
from config import USERS_FILE

#Funciones de Usuario
def add_user(name, age, city):
    users = load_file(USERS_FILE)
    new_id = max([i['user_id'] for i in users]) + 1 if users else 1
    new_user = {'user_id': new_id, 'name': name, 'age': age, 'city': city}
    users.append(new_user)
    save_file(users, USERS_FILE)
    return new_user

def get_user(get_id):
    users = load_file(USERS_FILE)
    for u in users:
        if u['user_id']==get_id:
            return u
    return None

def delete_user(delete_id):
    users = load_file(USERS_FILE)
    users_f = [u for u in users if u['user_id']!=delete_id]
    save_file(users_f,USERS_FILE)
    return
    
    
# Validation functions

def val_user(user_id):
    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        raise ValueError("ERROR: User ID must be a positive number.")
    if get_user(user_id) == None:
        raise ValueError(f"ERROR: User ID {user_id} does not exist.")
    return user_id

def val_age(age):
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise ValueError("ERROR: Age must be a positive number.")
    if age <= 0:
        raise ValueError("ERROR: Age must be a positive number.")
    return age