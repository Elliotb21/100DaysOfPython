# Acquiring the initial 25 colors and removing white/near white colors. Storing the tuples in a list
# import colorgram
# colors = colorgram.extract('damien-hirst-severed-spots.jpg', 25)
# rgb =[]
# for color_object in colors:
#     color_tuple = (color_object.rgb.r, color_object.rgb.g, color_object.rgb.b)
#     rgb.append(color_tuple)

# Goal is to recreate a Hirst painting. Our painting will be 10 x 10, with each penstroke 20, and 50 paces between
rgb_colors = [
    (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), 
    (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222), 
    (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9)
]
from turtle import Turtle, Screen
import random

# Initialize turtle object, screen object, and position turtle to start the drawing.
t = Turtle()
t.speed("fastest")
t.hideturtle()
t.pensize(20)
t.penup()
t.setposition(-250,-250)
t.pendown()
screen = Screen()
screen.colormode(255)


def draw_line():  
    """Draw a 20px dot from a random rgb_color."""  
    for circle in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.penup()
        t.forward(50)   


def restart_row():
    """move the turtle to the beginning of the row, and position 50 paces up from previous."""
    t.backward(50 * 10)
    t.left(90)
    t.forward(50)      
    t.right(90)         


# The whole drawing.
for _ in range(10):
    draw_line()
    restart_row()


screen.exitonclick()