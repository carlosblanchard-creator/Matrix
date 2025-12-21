import json
import os

# Load config
with open("config.json", "r") as config:
    config = json.load(config)

path = config["json_path"]

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

