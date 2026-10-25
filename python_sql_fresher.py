import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE test")

user = cursor.fetchall()
print(user)
connection.commit()

connection.close()  