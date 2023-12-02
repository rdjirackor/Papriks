import sqlite3 as s
import bcrypt
import tkinter as tk
from tkinter import simpledialog

def create_pass():
    password = simpledialog.askstring("Input", "Enter your password:")
    if password:
        static_salt = b'mein'
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) + static_salt
        return hashed_password
    else:
        return None

def insert_data():
    # Connect to the SQLite database (or create a new one if it doesn't exist)
    conn = s.connect('mydatabase.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Execute SQL commands
    cursor.execute('CREATE TABLE IF NOT EXISTS users (password VARCHAR(200) PRIMARY KEY)')

    # Insert data
    hashed_password = create_pass()
    if hashed_password:
        cursor.execute('INSERT INTO users VALUES (?)', (hashed_password,))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

def check_login():
    entered_password = simpledialog.askstring("Input", "Enter your password:")
    if entered_password:
        # Connect to the SQLite database
        conn = s.connect('mydatabase.db')
        cursor = conn.cursor()

        # Retrieve the stored hashed password from the database
        cursor.execute('SELECT password FROM users')
        result = cursor.fetchone()

        if result:
            stored_password = result[0]
            entered_password_bytes = entered_password.encode('utf-8')

            # Verify the entered password against the stored hash
            if bcrypt.checkpw(entered_password_bytes, stored_password):
                print("Login successful!")
            else:
                print("Login failed. Incorrect password.")

        # Close the connection
        conn.close()


# Create the main application window
app = tk.Tk()
app.title("Password Management")

# Set resizable to allow both horizontal and vertical resizing
app.resizable(True, True)

# Set the initial size of the window
app.geometry("1000x700")

# Create and pack a label
label = tk.Label(app, text="Click the button to enter your password:")
label.pack(pady=10)

# Create and pack buttons
button_create = tk.Button(app, text="Create Password", command=insert_data)
button_create.pack(pady=10)

button_login = tk.Button(app, text="Login", command=check_login)
button_login.pack(pady=10)

# Run the Tkinter event loop
app.mainloop()
