from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("blank")
timmy.pensize(width=5)
timmy.speed(8)
screen = Screen()
screen.colormode(255)
directions = [0,90,180,270]

def rgb():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return r, g, b

def random_walk(pen_color):
    timmy.color(pen_color)
    direction = random.choice(directions)
    timmy.setheading(direction)
    timmy.forward(50)
        
for _ in range(50):
    random_walk(rgb())
    





screen.exitonclick()
