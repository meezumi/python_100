from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)

def random_col():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)  

tim = Turtle()

tim.speed(0)
begin = tim.setheading(10)
i = 5
tim.circle(100)
tim.setheading(10)


while(tim.heading() != 0):
  tim.color(random_col())
  tim.circle(100)
  tim.setheading(10 + i)
  i += 5

tim.circle(100)









screen = Screen()
screen.exitonclick()