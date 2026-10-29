# Bad
class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency on concrete class

    def create_user(self, user_data):
        # Some business logic
        self.database.save(user_data)


# Good and follow DIP
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL database")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL database")

class MongoDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")

class UserService:
    def __init__(self, database: Database):
        self.database = database  # Depends on abstraction

    def create_user(self, user_data):
        # Some business logic
        self.database.save(user_data)

# Usage
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()
mongo_db = MongoDatabase()

user_service_mysql = UserService(mysql_db)
user_service_postgres = UserService(postgres_db)
user_service_mongo = UserService(mongo_db)

user_service_mysql.create_user("John Doe")
user_service_postgres.create_user("Jane Smith")
user_service_mongo.create_user("Bob Johnson")