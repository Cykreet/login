# cykreet/login ![hacktoberfest](https://img.shields.io/badge/-hacktoberfest-ff8cde?style=flat-square&logo=digitalocean&logoColor=9e4666)

simple command-line application made for fun and ᵃ ᶠʳᵉᵉ ᵗˢʰᶦʳᵗ with python, allowing a user to login with a username and password *or* create an account.

- while not an ideal solution, created users are stored in a json file in the project's root.
- stored passwords are hashed through [`bcrypt`](https://pypi.org/project/bcrypt/).
- once a user successfully logs in, they're introduced to their own "personal" hub, in which they can run certain commands.