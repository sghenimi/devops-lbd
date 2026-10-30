# Principe de responsabilité unique :
# Une classe doit avoir une seule raison de changer, c’est-à-dire une seule responsabilité.
# Meme logique pour les fonctions

from typing import Mapping


class Customer:
    pass

# Bad
def create_user_and_send_email(user: Customer) -> Mapping:
    ...

# Good
def create_user(user: Customer):
    ...

def send_email(user: Customer):
    ...

# 1. Single Responsibility Principle (SRP)
# Definition: A class should have only one reason to change, meaning it should have only one responsibility or job.
# Violating SRP
class User10:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        # Database logic
        print(f"Saving {self.name} to database")

    def send_email(self):
        # Email logic
        print(f"Sending email to {self.email}")

    def validate_email(self):
        # Validation logic
        return "@" in self.email

#Problems: The User class handles user data, database operations, email sending, and validation. It has multiple reasons to change.

# Following SRP
# Benefits: Each class now has a single responsibility, making the code more maintainable and testable.÷

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")

class EmailService:
    def send_email(self, user):
        print(f"Sending email to {user.email}")

class EmailValidator:
    @staticmethod
    def validate(email):
        if "@" in email:
            return True
        else:
            return False

if __name__ == '__main__':
    user = User("Bob", "bobgmail.com")
    if EmailValidator.validate(user.email):
        UserRepository().save(user)
        EmailService().send_email(user)
