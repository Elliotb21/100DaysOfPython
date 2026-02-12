from turtle import Turtle, Screen
import random

racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color from the rainbow! ")
if user_bet:
    racing = True

colors = ["red", "orange", "yellow", "blue", "indigo", "violet"]
all_turtles = []
num_turtles = len(colors)
height = 400
spacing = height / num_turtles
starting_y = (-height / 2) + (spacing / 2)

for index, color in enumerate(colors):
    turtle = Turtle(shape = "turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=starting_y + (index * spacing))
    all_turtles.append(turtle)

while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle was {winning_color}")
            else:
                print(f"You've lost. The winning turtle was {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()