from JSON_functions import load_file, save_file
from config import get_users_file
from datetime import datetime
import re

#Funciones de Usuario
def add_user(name, age, city, email, password):
    users = load_file(get_users_file())
    new_id = max([i['user_id'] for i in users]) + 1 if users else 1
    new_user = {'user_id': new_id, 'name': name, 'age': age, 'city': city, 'email': email, 'password':password, 'role':"user", 'created_at':datetime.now(), 'last_login': None}
    users.append(new_user)

    save_file(users, get_users_file())
    return new_user

def mod_user(mod_id, field, field_value):
    users = load_file(get_users_file())
    for u in users:
        if u['user_id']==mod_id:
            u[field]=field_value
            save_file(users, get_users_file())
            return u
    return None

def get_user(get_id):
    users = load_file(get_users_file())
    for u in users:
        if u['user_id']==get_id:
            return u
    return None

def get_user_by_email(get_email):
    users = load_file(get_users_file())
    for u in users:
        if u['email']==get_email:
            return u
    return None

def delete_user(delete_id):
    users = load_file(get_users_file())
    users_f = [u for u in users if u['user_id']!=delete_id]
    save_file(users_f,get_users_file())
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

# Validate email, to see if the email is valid. If new_user_flg = Y it checks if the email already exists in our DB (to avoid duplicates). If = N it does the opposite (it should exist in the DB)
def val_email(email, new_user_flg):
    email_norm = email.strip().lower()
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern,email_norm):
        raise ValueError("ERROR: Invalid email format")

    if new_user_flg == 'Y':
        if get_user_by_email(email_norm):
            raise ValueError("ERROR: email already exists")
    
    if new_user_flg == 'N':
        if get_user_by_email(email_norm) is None:
            raise ValueError("ERROR: email doesnt exist")
        
    return email_norm
    
    
def val_password(pwd, pwd2=None):
    if len(pwd) < 8:
        raise ValueError("ERROR: Password must have at least 8 characters.")
    if not re.search(r"[A-Z]",pwd) or not re.search(r"[a-z]",pwd):
        raise ValueError("ERROR: Password must contain at least one uppercase and one lowercase letter.")
    if not re.search(r"[0-9]",pwd):
        raise ValueError("ERROR: Password must contain at least one number")
    
    if pwd2 is not None and pwd != pwd2:
        raise ValueError("ERROR: Password must be the same.")
    
    return pwd

