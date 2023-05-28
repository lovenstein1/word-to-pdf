import sqlite3

# Соединение с базой данных (Создаст базу данных, если его нету)
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE users (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   email TEXT,
                   password TEXT)''')

# Insert some data into the table
cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", ("Alice", "alice@example.com", "password123"))
cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", ("Bob", "bob@example.com", "password456"))

# Commit the changes
conn.commit()

# Close the connection
conn.close()