from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
  tim.forward(10)
  
def move_backwards():
  tim.backward(10)

def move_left():
  tim.left(10)  
  
def move_right():
  tim.right(10) 
  
def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()
  
screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forwards) 
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

# when we pass a function inside a function, then we dont add () at the end of that function, like here in fun = move_forwards


screen.exitonclick()