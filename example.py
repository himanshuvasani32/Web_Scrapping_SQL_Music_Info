import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on a condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.14'")
rows = cursor.fetchall()
print(rows)

# Query certain column based on a certain condition
cursor.execute("SELECT band, city FROM events WHERE date='2088.10.14'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Lions', 'Lion City', '2088.10.15'),
            ('Cats', 'Cat City', '2088.10.15')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)