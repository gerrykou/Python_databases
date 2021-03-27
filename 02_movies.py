import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
('Back to the Future', 'Steven Spielberg', 1985),
('Moonrise Kingdom','Wes Anderson', 2012)]

cursor.executemany('Insert INTO Movies VALUES (?,?,?)', famousFilms)

records = cursor.execute("SELECT * FROM Movies")

print(cursor.fetchall())

connection.commit()
connection.close()


