from helpers import console
from hub.user import User
import hub.commands

class Hub:
  user: User

  def __init__(self, user: User):
    self.user = user

    console.clear()
    self.__home()

  def __home(self):
    console.message(f"Welcome Home, {self.user.username}!")
    self.__terminal()

  def __terminal(self):
    query = console.query('>')

    try:
      getattr(hub.commands, f"command_{query}")()
    except:
      console.message(f"Failed to run the '{query}' command. Make sure it exists by running 'help'.")

    self.__terminal()