from turtle import Turtle, Screen

# https://docs.python.org/3/library/turtle.html

baka = Turtle()
print(baka)
baka.shape("turtle")
baka.color("coral")
baka.fd(100)
my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
# the screen will exit when it detects a click

