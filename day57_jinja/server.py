from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)
# jinja only works with python

# https://genderize.io/
# https://agify.io/          all the used apis and json builders.
# https://www.npoint.io/

@app.route("/")
def home():
    my_name = "meezumi"
    current_year = datetime.datetime.now().year
    random_num = random.randint(1, 10)
    return render_template("index.html", num=random_num, year=current_year, name=my_name)


@app.route("/guess/<name>")
def gen_age(name):
    gen_response = requests.get(f"https://api.genderize.io?name={name}")
    gen_data = gen_response.json()
    gender = gen_data["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
