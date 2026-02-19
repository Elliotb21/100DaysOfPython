from turtle import Turtle

# Screen width is 600H x 800W
X_TOP_BOUND = 380
X_BOTTOM_BOUND = -380
Y_TOP_BOUND = 280
Y_BOTTOM_BOUND = -280
STEP = 25

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")        

        self.dx = 5
        self.dy = 5
        
    def move_ball(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
            
            
    def bounce_y(self):
        self.dy *= -1
        
            