from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("blank")
timmy.speed(0)
screen = Screen()
screen.colormode(255)


def rgb():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    return r, g, b

def draw_circle(gapsize):
    for _ in range(int(360 / gapsize)):
        timmy.color(rgb())
        timmy.circle(100.0)
        timmy.setheading(timmy.heading() + gapsize)  

draw_circle(10)



screen.exitonclick()
