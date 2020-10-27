from typing import List
from hub.user import User
from helpers import console

class CommandError(BaseException): ...
class CommandContext:
  def __init__(self, user: User, args: List[str]):
    self.user = user
    self.args = args

def command_clear(ctx: CommandContext):
  console.clear()

def command_hello(ctx: CommandContext):
  console.message(f"Hello, {ctx.user.username}!")

def command_echo(ctx: CommandContext):
  if not len(ctx.args) > 0:
    raise CommandError("You need to tell me what to echo!")

  console.message(" ".join(ctx.args))
