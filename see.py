import sqlite3
connection=sqlite3.connect('student.db')
cursor=connection.cursor()
cursor.execute('SELECT * FROM DETAILS')
r=cursor.fetchall()
print(r)
