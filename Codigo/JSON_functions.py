import json
import os

path = "JSON/"

#Acceso a ficheros JSON
def load_file(f_name):
    if os.path.exists(path+f_name):
        with open(path+f_name,"r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []
        return users
    return []

def save_file(content, f_name):
    with open(path+f_name,"w") as f:
        json.dump(content, f, indent=2, default=str)

