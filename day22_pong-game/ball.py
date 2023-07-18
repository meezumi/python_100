from turtle import Turtle


class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.move_speed = 0.05
  
  def move(self):
    new_x = self.xcor() + self.x_move   
    new_y = self.ycor() + self.y_move 
    self.goto(new_x, new_y)
    
  def move_back(self):
    # new_x = self.xcor() - 10
    # new_y = self.ycor() - 10 
    self.y_move *= -1
    # self.goto(new_x, new_y)
    
  def push_back(self):
    self.x_move *= -1 
    self.move_speed *= 0.9
    
  def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.push_back()