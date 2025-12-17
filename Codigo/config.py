import json

path = "JSON/"

with open(path+"config.json","r") as f:
    config = json.load(f)

ENV = config["ENV"]
CURRENT = config[ENV]

USERS_FILE = CURRENT["users_file"]
WORKOUTS_FILE = CURRENT["workouts_file"]