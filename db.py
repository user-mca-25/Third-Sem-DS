import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    password = 'password',
    database="mysql",
    user="root"
)

if conn.is_connected():
    print("Connected Successfully")

cur = conn.cursor()

cur.execute("Select * from studentn;")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute("INSERT INTO studentn(name,roll_no,course) VALUES ('qin shuhuang',5,'empire');")

conn.commit()

cur.execute("Select * from studentn;")

rows = cur.fetchall()

print()
print()


for row in rows:
    print(row)