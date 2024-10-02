# Filename: db.py
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

# Establish a connection to the MySQL database
def create_connection():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('books_db')
    db.setUserName('test')  # Replace with your MySQL username
    db.setPassword('test1234')  # Replace with your MySQL password
    if not db.open():
        print("Failed to connect to database.")
        return False
    return True

# Function to run a query and return a QSqlQuery instance
def get_author_data():
    query = QSqlQuery()
    query.exec("SELECT * FROM author")
    return query
