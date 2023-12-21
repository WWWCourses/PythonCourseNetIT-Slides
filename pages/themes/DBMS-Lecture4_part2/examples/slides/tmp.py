import mysql.connector

# Establish a connection to the MySQL server
db = mysql.connector.connect(
	host="localhost",
	user="test",
	password="test1234",
	database="test"
)

# Create a cursor object to interact with the database
cursor = db.cursor()


### Example: Fetching all rows
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
	print(row)

### Example:  Fetch a single row
cursor.execute("SELECT * FROM students")

row1 = cursor.fetchone()
row2 = cursor.fetchone()
print(row1)
print(row2)

db.close()

