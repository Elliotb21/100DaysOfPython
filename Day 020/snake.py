from turtle import Turtle, Screen
import time

class Snake:
    MOVE_DISTANCE = 20
    def __init__(self):
        STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_body = []
        
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.snake_body.append(segment)

    def move(self):
        for segment in range(len(self.snake_body) -1 , 0, -1):
            new_x = self.snake_body[segment -1].xcor()
            new_y = self.snake_body[segment -1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.snake_body[0].forward(self.MOVE_DISTANCE)    
