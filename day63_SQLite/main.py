import sqlite3

db = sqlite3.connect("books-collection.db")

# creating a new database with sqlite
# and if db doesn't exist, then it is created.

# next:
# a cursor is also known as the mouse or pointer. If we were working in
# Excel or Google Sheet, we would be using the cursor to add rows of data
# or edit/delete data, we also need a cursor to modify our SQLite database.

cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# this is to create table called books ^

# to create an entry to the table:
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

# close down the database in DB Browser by clicking Close Database.
# Otherwise, you'll get a warning about database locked when you work
# with the database in PyCharm.

# instead of typing out commands to create and add entries to sql
# databases, we will use python library sqlalcemy, less prone to
# making errors and easy to use