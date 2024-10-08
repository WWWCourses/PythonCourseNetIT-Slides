import mysql.connector

class DB:
    def __init__(self, user, password, db_name, host="localhost", port=3306):
        try:
            self.cnx = mysql.connector.connect(
                user=user, password=password, db=db_name, host=host, port=port
            )

        except mysql.connector.Error as e:
            print(f'Database Error: {e}')

        print("*** Connection Established ***")


    def authenticate(self, user_name, password):
        # Create a cursor for the connection
        with self.cnx.cursor() as cursor:
            # Prepare SQL query with placeholders to prevent SQL injection
            q = """
                SELECT * FROM users
                WHERE username = %s
                AND password = %s
            """

            # Execute the query with provided parameters
            cursor.execute(q, (user_name, password))

            # We are only interested if 1 or 0 rows are returned
            if cursor.fetchone():
                return True # Authentication successful

            return False  # Authentication failed


if __name__ == "__main__":
    db = DB('test', 'test1234','pyqt_users_db')
    is_authenticated = db.authenticate(user_name='Maria', password='maria123')

    if is_authenticated:
        print('Authentication successful!')
    else:
        print('Authentication failed!')
