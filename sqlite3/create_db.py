import sqlite3

conn = sqlite3.connect("example.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT not null,
        age INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

print("Database created successfully")


