from os import system, name
from getpass import getpass
import sys

def message(text: str):
  print(text)

def error(text: str, exit: bool = False):
  clear()
  message(text)

  if exit: sys.exit(1)

def query(text: str, pw: bool = False) -> str:
  text = text + " "
  if pw:
    return getpass(text)
  
  return input(text).strip().lower()

def exit(text: str):
  clear()
  message(text)

  sys.exit(0)

def clear():
  if name == 'nt':
    system('cls')
  else:
    system('clear')