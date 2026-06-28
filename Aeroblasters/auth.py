import json
import os

FILE_NAME = "users.json"

def load_users():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

def register(username, password):
    users = load_users()

    if username in users:
        return False

    users[username] = {
        "password": password,
        "highscore": 0,
        "skin": "default"
    }

    save_users(users)
    return True

def login(username, password):
    users = load_users()

    if username in users and users[username]["password"] == password:
        return True

    return False

def update_highscore(username, score):
    users = load_users()

    if username in users:
        if score > users[username]["highscore"]:
            users[username]["highscore"] = score
            save_users(users)

def get_highscore(username):
    users = load_users()

    if username in users:
        return users[username]["highscore"]

    return 0

def get_skin(username):
    users = load_users()

    if username in users:
        return users[username].get("skin", "default")

    return "default"

def update_skin(username, skin):
    users = load_users()

    if username in users:
        users[username]["skin"] = skin
        save_users(users)