import psycopg2

conn = psycopg2.connect(
    dbname='example_db',
    user = 'example_user',
    password = 'password',
    host = 'localhost',
    port = 5432
)

cursor = conn.cursor()

cursor.execute(''' 
    SELECT * FROM users;
''')

users = cursor.fetchall()

for user in users:
    print(user)



    