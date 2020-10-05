from types import coroutine
from helpers import console
from enum import Enum
from hub.hub import Hub
from hub.user import User
import json
import bcrypt

with open ("users.json") as users:
  users = json.load(users)

class Mode(Enum):
  LOGIN = "1"
  CREATE = "2"

class Query:
  mode: str
  user: User

  def __init__(self):
    self.user = User()

  def start(self):
    valid = False
    while not valid:
      mode = console.query(f"Please specify whether you'd like to (1, default) login or (2) create an account:")
      if mode == Mode.LOGIN.value or mode == Mode.CREATE.value or not mode:
        valid = True
        self.mode = mode if mode else Mode.LOGIN.value

        console.clear()
        self.__username()
    
      console.clear()

  def __username(self):
    valid = False
    while not valid:
      username = console.query("Username:")
      if self.mode == Mode.CREATE.value:
        # todo
        console.error("Work in progress..", True)

      if username in users:
        valid = True
        self.user.username = username
        self.user.password = users[username]["password"]

        console.clear()
        self.__password()

      console.error("That user doesn't exist.")
      
  def __password(self):
    valid = False
    while not valid:
      password = console.query(f"{self.user.username}'s Password:", True)
      if self.mode == Mode.CREATE.value:
        # todo
        console.error("Work in progress...", True)

      if bcrypt.checkpw(password.encode(), self.user.password.encode()):
        valid = True
        Hub(self.user)
        
      console.error("Incorrect password, please try again.")