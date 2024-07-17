# db/operations.py

import mysql.connector
from mysql.connector import Error
from .config import db_config

class MySQLDB:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: '{e}'")
        return connection

    def create_user(self, name, email):
        cursor = self.connection.cursor()
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        self.connection.commit()
        print("User created successfully")

    def get_users(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        for user in users:
            print(user)

    def update_user_email(self, user_id, new_email):
        cursor = self.connection.cursor()
        query = "UPDATE users SET email = %s WHERE id = %s"
        cursor.execute(query, (new_email, user_id))
        self.connection.commit()
        print("User email updated successfully")

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        self.connection.commit()
        print("User deleted successfully")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
