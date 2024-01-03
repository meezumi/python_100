from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# data entry should be added to the list in the form of dictionary like:
#
# all_books = [
#     {
#         "title": "",
#         "author": "",
#         "rating": 8,
#     }
# ]

all_books = []

# if we refresh the page, stop the server and restart it, all
# the entries will be lost, so we need a backend
# database for data storage permanently


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

