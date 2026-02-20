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
        self.ball_speed = 0.03       

        self.x = 5
        self.y = 5
        
    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)
            
            
    def bounce_y(self):
        self.y *= -1
        
    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= 0.75
        
    
    def reset_ball(self):
        self.goto(0,0)
        self.ball_speed = 0.03
        self.bounce_x()
        
            