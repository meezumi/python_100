from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)
print(__name__)


@app.route("/")
def guess_num():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/137qIhWsIf9bDW/giphy.gif"> ')


@app.route("/<int:guess>")
def higher(guess):
    if guess > random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/eSwGh3YK54JKU/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/aDS8SjVtS3Mwo/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
