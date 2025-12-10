from JSON_functions import load_file, save_file

File_name = "users.json"

#Funciones de Usuario
def add_user(name, age, city):
    users = load_file(File_name)
    new_id = max([i["id"] for i in users]) + 1 if users else 1
    try:
        new_user = {"id": new_id, "name": name, "age": val_age(age), "city": city}
    except ValueError as e:
        print(e)
        return None
    users.append(new_user)

    save_file(users, File_name)
    
    print(f"New user, {new_user['name']}, added successfully with ID {new_user['id']}")
    return new_user

def get_user(get_id):
    users = load_file(File_name)
    for u in users:
        if u["id"]==get_id:
            return u
    return None

def delete_user(delete_id):
    users = load_file(File_name)
    try:
        del_id = val_user(delete_id)
    except ValueError as e:
        print(e)
        return False
    
    users_f = [u for u in users if u["id"]!=del_id]
    save_file(users_f,File_name)

    print(f"User ID {delete_id} was deleted successfully.")
    return True
    
    
# Validation functions

def val_user(user_id):
    if get_user(user_id) == None:
        raise ValueError(f"User {user_id} does not exist.")
    return user_id

def val_age(age):
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise ValueError("Age must be a positive number.")
    if age <= 0:
        raise ValueError("Age must be a positive number.")
    return age