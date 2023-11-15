from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive():
    user = request.form['username']
    passs = request.form['pass']
    return (f"successfully logged in...your mom"
            f"Name: {user}, password: {passs}")

# using all the knowledge here we go back to day60


if __name__ == "__main__":
    app.run(debug=True)

