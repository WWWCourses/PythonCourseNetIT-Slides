# db/operations.py

import mysql.connector
from mysql.connector import Error
from .config import db_config

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def create_user(connection, name, email):
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    connection.commit()
    print("User created successfully")

def get_users(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    for user in users:
        print(user)

def update_user_email(connection, user_id, new_email):
    cursor = connection.cursor()
    query = "UPDATE users SET email = %s WHERE id = %s"
    cursor.execute(query, (new_email, user_id))
    connection.commit()
    print("User email updated successfully")

def delete_user(connection, user_id):
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print("User deleted successfully")
