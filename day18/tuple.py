from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b) 
# this is a tuple

# python tuple
(1, 3, 8) 
# you cant change the value in tuples in anyway (immutable)

tim = Turtle()

tim.color(random_color())
tim.width(10)
tim.forward(100)


# python list
[1, 3, 4]
# but you can change the value in lists (mutable)

# to change a tuple, just put the tuple inside the list like:
  # list(my_tuple)
  

screen = Screen()
screen.exitonclick()