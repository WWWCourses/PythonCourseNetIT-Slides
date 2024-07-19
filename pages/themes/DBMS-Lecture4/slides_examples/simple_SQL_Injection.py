import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host='test',
    user='test1234',
    password='your_password',
    database='your_database'
)

cursor = connection.cursor()

# User input (in a real application, this would come from a form or user input)
username = input("Enter your username: ")
password = input("Enter your password: ")

# Insecure query construction prone to SQL injection
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

print("Constructed Query: " + query)  # For demonstration purposes, print the constructed query

cursor.execute(query)

# Fetch the result
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

# Close the cursor and connection
cursor.close()
connection.close()
