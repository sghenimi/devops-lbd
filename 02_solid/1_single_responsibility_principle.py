# Principe de responsabilité unique :
# Une classe doit avoir une seule raison de changer, c’est-à-dire une seule responsabilité.
# Meme logique pour les fonctions

from typing import Mapping


class User:
    pass

# Bad
def create_user_and_send_email(user: User) -> Mapping:
    ...

# Good
def create_user(user: User):
    ...

def send_email(user: User):
    ...