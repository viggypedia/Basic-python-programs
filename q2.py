import sqlite3

#By: S.Vignesh Nelakantan
#Reg.No:RA2011003001530

# Connect to database
connection = sqlite3.connect('q2.db')

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("CREATE TABLE movies (movie_id integer, movie_name text, genre text, language text, rating real)")

# insert data
movies = [
    (101, "kgf2", "action", "hindi", 8.5),
    (102, "spiderman", "superhero", "english", 8.1),
    (103, "doctor strange", "mystic", "english", 8.7),
]

cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", movies)

# query to db
cursor.execute("UPDATE movies SET rating = (rating + (rating * 0.1))")
cursor.execute("SELECT movie_name, rating from movies")
movies = cursor.fetchall()
print(movies)
print('-----------------------------------------------------')

# delete db
cursor.execute("DELETE from movies WHERE movie_id = 102")
cursor.execute("SELECT * FROM movies")
d = cursor.fetchall()
print(d)
print('-----------------------------------------------------')

cursor.execute("SELECT movie_name, rating FROM movies WHERE rating > 3")
r = cursor.fetchall()
print(r)
print('-----------------------------------------------------')

# Commit changes
connection.commit()

# Close connection
connection.close()

