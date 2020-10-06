from os import system, name
from getpass import getpass
import sys

def message(text: str):
  print(text)

def error(text: str, exit: bool = False):
  clear()
  message(text)

  if exit: sys.exit(1)

def query(text: str, password = False, ignore_case = False) -> str:
  text = text + " "
  if password:
    return getpass(text)
  
  out = input(text).strip()
  return out.lower() if not ignore_case else out

def exit(text: str):
  clear()
  message(text)

  sys.exit(0)

def clear():
  if name == 'nt':
    system('cls')
  else:
    system('clear')