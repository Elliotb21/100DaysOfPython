from turtle import Turtle, Screen

turk = Turtle()
turk.pendown()
turk.pensize(5)
screen = Screen()  

def move_forward():
    turk.forward(10)
    
def turn_right():
    turk.right(15)
    
def turn_left():
    turk.left(15)
    
def move_backwards():
    turk.backward(10)

def clear():
    turk.clear()
    turk.penup()
    turk.home()
    turk.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=clear, key="c")


screen.exitonclick()