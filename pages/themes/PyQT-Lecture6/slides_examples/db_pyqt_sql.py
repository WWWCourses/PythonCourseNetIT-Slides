from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class DB:
    def __init__(self, user, password, db_name, host="localhost", port=3306):
        # Specify MySQL as the database type
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName(host)
        db.setDatabaseName(db_name)
        db.setUserName(user)
        db.setPassword(password)

        if db.open():
            print("*** Connection Established ***")
        else:
            print(f"Database Error: {db.lastError().text()}")

    def authenticate(self, user_name, password):
        query = QSqlQuery()

        # Prepare SQL query with placeholders to prevent SQL injection
        query.prepare("""
            SELECT * FROM users
            WHERE username = :username
            AND password = :password
        """)

        # bind with provided parameters
        query.bindValue(":username", user_name)
        query.bindValue(":password", password)

        if query.exec():
            if query.next():  # If at least one row is returned
                return True  # Authentication successful
        return False  # Authentication failed


if __name__=="__main__":
    db = DB('test', 'test1234','pyqt_users_db')
    is_authenticated = db.authenticate(user_name='Maria', password='maria123')

    if is_authenticated:
        print('Authentication successful!')
    else:
        print('Authentication failed!')


