import json
import os

def set_environment(env): #1 == PROD; 2 == DEV
    global ENV, USERS_FILE, WORKOUTS_FILE

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(BASE_DIR,"config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    if env == 1:
        ENV = "PROD"
    if env == 2:
        ENV = "DEV"
    
    config["ENV"] = ENV
    
    CURRENT = config[ENV]

    USERS_FILE = CURRENT["users_file"]
    WORKOUTS_FILE = CURRENT["workouts_file"]

    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)