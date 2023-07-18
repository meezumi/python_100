from turtle import Turtle, Screen
from ball import Ball
from slider import Slider
import time
from scoreboard import Scoreborad

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Slider((-350, 0))
player_2 = Slider((350, 0))
ball = Ball() 
scoreboard = Scoreborad()

 
screen.listen()
screen.onkeypress(player_1.up, "w")
screen.onkeypress(player_1.down, "s")
screen.onkeypress(player_2.up, "Up")
screen.onkeypress(player_2.down, "Down") 

# player-2 right and player-1 left

game_on = True
while game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()
  
  # detect collision with wall 
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.move_back()

  # detect collision with the slider
  if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
    ball.push_back() 
    
  # when player 2 misses   
  if ball.xcor() > 380: 
      ball.reset_position()
      scoreboard.l_point()
  
  if ball.xcor() < -380:
      ball.reset_position()   
      scoreboard.r_point() 














screen.exitonclick()

