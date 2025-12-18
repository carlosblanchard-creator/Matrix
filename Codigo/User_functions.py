from JSON_functions import load_file, save_file
from config import USERS_FILE
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import re

#Funciones de Usuario
def add_user(name, age, city, email, password):
    users = load_file(USERS_FILE)
    new_id = max([i['user_id'] for i in users]) + 1 if users else 1
    new_user = {'user_id': new_id, 'name': name, 'age': age, 'city': city, 'email': email, 'password':password, 'role':"user", 'created_at':datetime.now(), 'last_login': None}
    users.append(new_user)

    save_file(users, USERS_FILE)
    return new_user

def mod_user(mod_id, field, field_value):
    users = load_file(USERS_FILE)
    for u in users:
        if u['user_id']==mod_id:
            u[field]=field_value
            save_file(users, USERS_FILE)
            return u
    return None

def get_user(get_id):
    users = load_file(USERS_FILE)
    for u in users:
        if u['user_id']==get_id:
            return u
    return None

def get_user_by_email(get_email):
    users = load_file(USERS_FILE)
    for u in users:
        if u['email']==get_email:
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

def val_email(email, new_user_flg):
    try:
        valid = validate_email(email)
        email_norm = valid.email
    except EmailNotValidError as e:
        raise ValueError(str(e))
    
    if new_user_flg == 'Y':
        if get_user_by_email(email_norm):
            raise ValueError("ERROR: email already exists")
        
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