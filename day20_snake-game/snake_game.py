from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scorboard import Scoreboard

food = Food()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.title("Snake Game")
screen.tracer(0)
# turns the animation on or off
# dimension of snake is 20x20


snake = Snake()
scoreboard = Scoreboard() 


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
  

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  # for seg in segments:
  #   seg.forward(20)
  snake.move()

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
    
  # detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    # game_on = False
    # scoreboard.game_over()
    scoreboard.reset()


  # detect collision with the body of the snake
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      # game_on = False
      # scoreboard.game_over()              
        scoreboard.reset()        
                  
                  
    


    







screen.exitonclick()





# what i used 

# x_at = 0
# for snake_l in range(0,3):
#   new_snake = Turtle(shape="square")
#   new_snake.penup()
#   new_snake.color("white")
#   new_snake.goto(x = x_at, y=0)
#   x_at -= 20 
#   segments.append(new_snake)
  