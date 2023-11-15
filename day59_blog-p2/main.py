from flask import Flask, render_template, request
import requests
import smtplib

my_email = "malifemarules7@gmail.com"
password = "fwpf lewk ikot nhvd"

app = Flask(__name__)

# https://api.npoint.io/ee7cd0f399bc65748175
# response = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
# blog_data = response.json()


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def read_more(index):
    blog_url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(blog_url)
    all_posts = response.json()
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        u_name = request.form["name"]
        u_email = request.form["email"]
        u_phone = request.form["phone"]
        u_message = request.form["message"]
        # return f"<h1> {u_name} </h1>"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            # to start the transport layer security, to secure the connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="kenkinkun123@yahoo.com",
                                msg=f"Subject:Hello\n\n{u_message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
    # u_name = request.form["name"]
    # u_email = request.form["email"]
    # u_phone = request.form["phone"]
    # u_message = request.form["message"]
    # return f"<h1> {u_name} </h1>"


if __name__ == "__main__":
    app.run(debug=True)


