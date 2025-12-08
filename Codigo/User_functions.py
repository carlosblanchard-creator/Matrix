from JSON_functions import load_file, save_file

File_name = 'users.json'

#Funciones de Usuario
def create_user(name, age, city):
    users = load_file(File_name)
    new_id = max([i['id'] for i in users]) + 1 if users else 1
    new_user = {"id": new_id, "name": name, "age": age, "city": city}
    users.append(new_user)

    save_file(users, File_name)
    
    print(f"New user, {new_user['name']}, added successfully with ID {new_user['id']}")
    return new_user

def get_user(get_id):
    users = load_file(File_name)
    for u in users:
        if u['id']==get_id:
            return u
    return None

def delete_user(delete_id):
    users = load_file(File_name)
    users_f = [u for u in users if u['id']!=delete_id]
    if len(users) == len(users_f):
        print(f"User ID {delete_id} was not found")
        return False
    else:
        save_file(users_f,File_name)
        print(f"User ID {delete_id} was deleted successfully")
        return True
    


