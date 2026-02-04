from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
screen = Screen()
screen.colormode(255)

def rgb():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return r, g, b


def draw_shape(num_sides, pen_color):
    timmy.color(pen_color)
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
        
for shape in range(3,11):
    draw_shape(shape, rgb())
    

screen.exitonclick()
