STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def place_back(self):
        self.goto(STARTING_POSITION)    
