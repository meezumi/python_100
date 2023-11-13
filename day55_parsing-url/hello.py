from flask import Flask
app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">hello everyneon!</h1>'
            '<p>nyeownom</p>'
            '<img src="https://media.giphy.com/media/Puc4FZWExJc0E/giphy.gif" width=200>')


# @app.route("/username/<name>")
# def greet(name):
#     return f"hello {name}"


@app.route("/username/<name><int:number>")
def greet(name, number):
    return f"hello {name}, you are {number} years old."


@app.route("/bye")
def bye():
    return "<b>bye bye everonemeow</b>,"


if __name__ == "__main__":
    app.run(debug=True)

