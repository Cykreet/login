from bcrypt import hashpw, gensalt
import json

class User:
  username: str
  password: str

  def save(self):
    with open("users.json", "r+") as users:
      data = json.load(users)
      data.update({ self.username: { "password": hashpw(self.password.encode(), gensalt()).decode() }})
      users.seek(0)
      json.dump(data, users)