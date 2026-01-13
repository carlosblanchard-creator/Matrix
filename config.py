import json
import os

_config = {}
_env_name = None

def set_environment(env): #1 == PROD; 2 == DEV
    global _config, _env_name

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(BASE_DIR,"config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    _env_name = "PROD" if env == 1 else "DEV"
    
    config["ENV"] = _env_name
    _config = config[_env_name]

    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

def get_users_file():
    return _config.get("users_file")

def get_workouts_file():
    return _config.get("workouts_file")

def get_env():
    return _env_name