from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "magenta", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    car_speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2.5, stretch_wid= 1, outline=1)
        self.color(choice(COLORS))
        self.goto(300, self.starting_y())
   
   
    def starting_y(self):
        return randint(-250, 250)
        
        
    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x - self.car_speed
        self.goto(new_x, current_y)
        
        
    def next_level(self):
        CarManager.car_speed += MOVE_INCREMENT