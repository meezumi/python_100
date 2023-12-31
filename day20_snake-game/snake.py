from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
# constants (always in cap)


class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
    
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)
  
  def add_segment(self, position):
      new_segment = Turtle(shape="square")
      new_segment.penup()
      new_segment.color("white")         
      new_segment.goto(position)
      self.segments.append(new_segment)
      
  def extend(self):
    #  add a new segment to the snake 
      self.add_segment(self.segments[-1].position())
      # in list of python you can count starting for the end of the list using negative number
      
  def move(self):
    #                           (start,stop,step)
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
      
  def reset(self): 
    for seg in self.segments:
      seg.goto(1000,1000)
    self.segments.clear() 
    self.create_snake()
    self.head = self.segments[0]
      
    
    self.head.forward(MOVE_DISTANCE)
    # making the last segment come to the last second position of the whole body and follwing this through out the snake
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
    
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
    