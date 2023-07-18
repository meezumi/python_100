from turtle import Turtle
import random


class Food(Turtle):
  
  def __init__(self):
    super().__init__()
  #  Turtle is the super class 
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=1, stretch_wid=1)
    # from 20x20 to 10x10
    self.color("blue")
    self.speed("fastest")
    self.refresh()
    
    
  def refresh(self):  
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)
    