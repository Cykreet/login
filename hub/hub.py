from helpers import console
from hub.commands import CommandContext, CommandError
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
    query = console.query('>', False, True).split()
    command = query[0].lower()

    try:
      getattr(hub.commands, f"command_{command}")(CommandContext(self.user, query[1:]))
    except CommandError as e:
      console.message(f"Failed to run the '{command}' command:\n{e}")
    except:
      console.message(f"Failed to run the '{command}' command. Make sure it exists by running 'help'.")

    self.__terminal()