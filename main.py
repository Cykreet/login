from os import system, name
from time import sleep
import bcrypt
import getpass
import json
import sys

with open("users.json") as users:
    users = json.load(users)


def askUsername():
    global username
    correctUser = False
    while not correctUser:
        username = lineInput("Please input username: ")
        if username in users:
            clear()
            askPass(username)
        else:
            clear()
            print(f"User, '{username}' does not exist.")


def askPass(username):
    correctPW = False
    while not correctPW:
        password = getpass.getpass(f"Please input password for {username}: ")
        display_name = users[username]["display_name"]
        if not bcrypt.checkpw(
            password.encode("utf8"), users[username]["password_hash"].encode("utf8")
        ):
            clear()
            print("Incorrect password, please try again.")
        else:
            correctPW = True
            home(display_name)


def home(display_name):
    clear()
    print(f"Welcome back, {display_name}!")

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
        print(
            f"- profile\noutputs your profile\n- clear\nclears terminal\n- exit\nexits login app"
        )
        commands(username)
    elif command == "profile":
        print(
            f"//////////\nDisplay Name: {display_name}\nUsername: {username}\nLocation: {location}\nDescription: {description}\n//////////"
        )
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
        print(
            f"Couldn't find the '{command}' command. Please try another or do 'help' to view all available commands!"
        )
        commands(username)


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def lineInput(upString):
    output = input(upString).strip()

    return output


if __name__ == "__main__":
    clear()
    askUsername()
