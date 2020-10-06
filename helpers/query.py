from typing import Any, IO
from helpers import console
from enum import Enum
from hub.hub import Hub
from hub.user import User
import json
import bcrypt

users: Any

try:
  users = json.load(open("users.json"))
except:
  users = json.dump(dict(), open("users.json", "w"))

class Mode(Enum):
  LOGIN = "1"
  CREATE = "2"

class Query:
  mode: str
  user = User()

  def start(self):
    while True:
      mode = console.query(f"Please specify whether you'd like to (1, default) login or (2) create an account:")
      if mode == Mode.LOGIN.value or mode == Mode.CREATE.value or not mode:
        self.mode = mode if mode else Mode.LOGIN.value

        console.clear()
        self.__username()
        break
    
      console.clear()

  def __username(self):
    while True:
      username = console.query("Username:")
      if self.mode == Mode.CREATE.value:
        self.user.username = username

        console.clear()
        self.__password()
        break

      if len(users) > 0 and username in users:
        self.user.username = username
        self.user.password = users[username]['password']

        console.clear()
        self.__password()
        break

      console.error("That user doesn't exist.")
      
  def __password(self):
    while True:
      password = console.query(f"{self.user.username}'s Password:", True)
      if self.mode == Mode.CREATE.value:
        self.user.password = password
        self.user.save()

        Hub(self.user)
        break

      if bcrypt.checkpw(password.encode(), self.user.password.encode()):
        Hub(self.user)
        break
        
      console.error("Incorrect password, please try again.")