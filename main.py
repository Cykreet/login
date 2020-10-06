from helpers.query import Query
from helpers.console import clear, error

if __name__ == "__main__":
  try:
    clear()
    Query().start()
  except KeyboardInterrupt:
    error("Quitting...", True)