from helpers import console
from enum import Enum
from getpass import getpass
import json
import bcrypt

with open ("users.json") as users:
  users = json.load(users)

class Mode(Enum):
  LOGIN = "1"
  CREATE = "2"

class Query:
  mode: str
  username: str

  def start(self):
    while True:
      mode = console.query(f"Please specify wheter you'd like to (1) login or (2) create an account:")
      if mode == Mode.LOGIN.value or mode == Mode.CREATE.value:
        self.mode = mode

        console.clear()
        self.__username()
    
      console.clear()

  def __username(self):
    while True:
      username = console.query("Username:")
      if self.mode == Mode.CREATE.value:
        # todo
        console.error("Work in progress..", True)

      if username in users:
        self.username = username

        console.clear()
        self.__password()

      console.error("That user doesn't exist.")
      
  def __password(self):
    while True:
      password = getpass(f"{self.username}'s Password:")
      if self.mode == Mode.CREATE.value:
        # todo
        console.error("Work in progress...", True)

      if bcrypt.checkpw(password.encode('utf8'), users[self.username]['password'].encode('utf8')):
        console.exit(f"Logged in as {self.username}")

      console.error("Incorrect password, please try again.")