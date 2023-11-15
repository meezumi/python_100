from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# to simply edit this page just being in the browser, open console and use:
# document.body.contentEditable=true
if __name__ == "__main__":
    app.run(debug=True)
