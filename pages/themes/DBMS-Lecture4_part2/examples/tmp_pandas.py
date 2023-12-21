import mysql.connector
import pandas as pd

# Establish a connection to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test1234",
    database="test"
)

# Define the SQL query to select data from the 'students' table
query = "SELECT * FROM students"

# Read data from the MySQL database directly into a Pandas DataFrame
df = pd.read_sql(query, con=db)

# Display the DataFrame
print(df)

# Close connection
db.close()
