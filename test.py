import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the query to select the password
cursor.execute("SELECT password FROM users")

# Fetch the result
password = cursor.fetchall()

# Display the password
print(password)

# Close the cursor and connection
cursor.close()
conn.close()
