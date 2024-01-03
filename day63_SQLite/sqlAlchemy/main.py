from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# reading the documentation from:
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)


# this creates the table schema in the database.
with app.app_context():
    db.create_all()




# creating an entry/record in the table:
# with app.app_context():
#     new_book = Book(id=1, title="only partially", author="drake", rating=9.3)
#     # entering values for the column names one by one
#     db.session.add(new_book)
#     # adding this new_book into the database/library/table
#     db.session.commit()
#     # saving the changes

# TO READ ALL THE RECORDS IN THE TABLE: scalers()
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()
#
# # TO READ A PARTICULAR RECORD BY QUERY: scaler()
#
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "only partially")).scalar()
#
#
# # TO UPDATE A PARTICULAR RECORD BY QUERY:
#
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
# # TO UPDATE BY PRIMARY KEY:
#
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()
#
# # TO DELETE A RECORD BY PRIMARY KEY:
#
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()

