from psycopg2 import connect, OperationalError
from dotenv import load_dotenv, dotenv_values
import os

# Load environment variables from .env file
load_dotenv()

print(type(dotenv_values(".env")))
conn_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = connect(**conn_params)
            print("Connection successful")
        except OperationalError as error:
            print(f"Error connecting to the database: {error}")
            self.connection = None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def execute_query(self, query):
        if self.connection:
            cursor = self.connection.cursor()  # Create cursor without `with`
            cursor.execute(query)
            return cursor
             
