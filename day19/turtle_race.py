from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"] 
all_turtle = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
print(user_bet)

# new_turtle.penup()
# new_turtle.goto(x=-230, y=-100)
# i = 0
y_at = -100
for turtle_i in range(0, 6):
  # range is not inclusive
  new_turtle = Turtle(shape="turtle")
  new_turtle.penup()
  new_turtle.color(colors[turtle_i])
  # i += 1
  new_turtle.goto(x=-230, y=y_at)
  y_at += 30
  all_turtle.append(new_turtle)
  

if user_bet:
  is_race_on = True
  
while is_race_on:
  for turtle in all_turtle:
    if turtle.xcor() > 230:
      is_race_on = False
      won = print(turtle.pencolor())
      if won == user_bet:
        print("you won the bet!")
      else:
        print("you lose the bet :)")
    random_dist = random.randint(0,10)
    # randint is inclusive
    turtle.forward(random_dist)



screen.exitonclick()