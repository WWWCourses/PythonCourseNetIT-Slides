# main.py

from db.operations import create_connection, create_user, get_users, update_user_email, delete_user

def main():
    connection = create_connection()

    if connection is not None:
        # Create a user
        create_user(connection, "Ivan Ivanov", "ivan.ivanov@example.com")

        # Read users
        print("Users:")
        get_users(connection)

        # Update a user's email
        update_user_email(connection, 1, "ivan.newemail@example.com")

        # Read users again to see the update
        print("Updated Users:")
        get_users(connection)

        # Delete a user
        delete_user(connection, 1)

        # Read users again to see the deletion
        print("Users after deletion:")
        get_users(connection)

        connection.close()

if __name__ == "__main__":
    main()
