
from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
# to setting it in a random direction we can use setheading()

tim = Turtle()

tim.width(10)
tim.speed(10)

for _ in range(200):
  tim.forward(10)
  tim.setheading(random.choice(directions))
  tim.color(random.choice(colours))
  tim.forward(10)



screen = Screen()
screen.exitonclick()