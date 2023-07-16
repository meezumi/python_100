from turtle import Turtle, Screen


# timmy = Turtle()
# # new turtle object 

                            # # to make a square 
# for move in range(4):
#   timmy.forward(100)
#   timmy.right(90)
  
# we can give alias to the modules imported 
# import turtle as t
#
# tim = t.Turtle()

                            # to make a dash linee 
import random 
timmy = Turtle()

# for move in range(15):
#   timmy.fd(15)
#   timmy.color("white")
#   timmy.fd(15)
#   timmy.color("black")  
  
# or 

# for move in range(10):
#   timmy.forward(10)
#   timmy.penup()
#   timmy.forward(10)
#   timmy.pendown()

# to make shapes till 10 equal sides: decagon 

i = 3
while i!=11:
  for move in range(i):
    # timmy.color(random.choice()) to randomize color 
    timmy.forward(100)
    timmy.right(360/i)
  
  i += 1





















screen = Screen()
screen.exitonclick()
