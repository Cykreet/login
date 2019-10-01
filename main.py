from passlib.hash import pbkdf2_sha256
from os import system, name
from time import sleep
import getpass
import json
import sys

with open("users.json") as users:
    users = json.load(users)

def askUsername():
    global username
    username = lineInput("Please input username: ")

    while username not in users:
        clear()
        print(f"User, '{username}' does not exist.")
        askUsername()

    clear()
    askPass(username)

def askPass(username):
    password = getpass.getpass(f"Please input password for {username}: ")
    display_name = users[username]["display_name"]

    if pbkdf2_sha256.verify(password, users[username]["password_hash"]):
        home(display_name)
    else: 
        clear()
        print("Incorrect password, please try again.")
        askPass(username)

def home(display_name):
    clear()
    print(f"Welcome back {display_name}!")

    commands(username)

def commands(username):
    command = lineInput(f"Input command: ").lower()

    display_name = users[username]["display_name"]
    location = users[username]["location"]
    description = users[username]["description"]

    if not description:
        description = "None set."
    elif not location:
        location = "None set."
        
    if command == "help":
        print("i'm too lazy")
        commands(username)
    elif command == "profile":
        print(f"//////////\nDisplay Name: {display_name}\nUsername: {username}\nLocation: {location}\nDescription: {description}\n//////////")
        commands(username)
    elif command == "clear":
        clear()
        commands(username)
    elif command == "exit":
        print("Exiting...")
        sleep(1)
        clear()
        sys.exit(1)
    else:
        print(f"Couldn't find '{command}' command.")
        commands(username)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def lineInput(upString):
    output = input(upString).strip()

    return output

clear()
askUsername()