import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO users (id, name, age) VALUES (1, 'Alice', 25)
''')
cursor.execute('''
    INSERT INTO users (id, name, age) VALUES (2, 'Ranjith', 23)
''')
cursor.execute('''
    INSERT INTO users (id, name, age) VALUES (3, 'Bob', 12)
''')

conn.commit()
conn.close()

print("Data Inserted Successfully")


