# main.py

from db.operations import MongoDB

def main():
    db = MongoDB()

    # Create a user
    db.create_user("Ivan Ivanov", "ivan.ivanov@example.com")

    # Read users
    print("Users:")
    db.get_users()

    # Update a user's email
    # Replace with actual user ID from the database
    user_id = input("Enter user ID to update: ")
    db.update_user_email(user_id, "ivan.newemail@example.com")

    # Read users again to see the update
    print("Updated Users:")
    db.get_users()

    # Delete a user
    user_id = input("Enter user ID to delete: ")
    db.delete_user(user_id)

    # Read users again to see the deletion
    print("Users after deletion:")
    db.get_users()

if __name__ == "__main__":
    main()
