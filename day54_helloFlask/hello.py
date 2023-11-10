from flask import Flask

app = Flask(__name__)
print(__name__)
# it runs from a script, from an interactive prompt but
# not from an imported module


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/bye')
def say_bye():
    return "boi boii"


if __name__ == "__main__":
    app.run()
# this is basically typed version of: flask run


# flash just converts our code into html for the internet
# to remove a file we use rm filename
# to remove a folder we use rm -rf filename


# def outer_function():
#     print("im outer")
#
#     def nested_function():
#         print("im inner")
#
#     nested_function()
#
#
# outer_function()
#
# def new():
#     print("naice")
#
#     def nested_new():
#         print("job")
#
#     return nested_new
#
# nested_new = new()
#
# nested_new()
