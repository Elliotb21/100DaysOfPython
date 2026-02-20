from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        
    
    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        new_y = current_y + MOVE_DISTANCE
        self.goto(current_x, new_y)


    def safely_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        
        
    def reset(self):
        self.goto(STARTING_POSITION)