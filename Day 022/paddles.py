from turtle import Turtle

# Screen width is 600H x 800W

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4.0, stretch_len=1, outline=0)
        self.penup()
        self.goto(position)
        
 