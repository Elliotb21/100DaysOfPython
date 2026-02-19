from turtle import Turtle

# Screen width is 600H x 800W
TOP_BOUND = 250
BOTTOM_BOUND = -250
STEP = 25

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5.0, stretch_len=1, outline=0)
        self.penup()
        self.goto(position)
        
    
    def move_paddle(self, step_direction):
        new_y = self.ycor() + step_direction
        # Clamp to screen bounds
        if new_y > TOP_BOUND:
            new_y = TOP_BOUND
        if new_y < BOTTOM_BOUND:
            new_y = BOTTOM_BOUND

        self.goto(self.xcor(), new_y)
        
    def paddle_up(self):
        self.move_paddle(STEP)
        
    def paddle_down(self):
        self.move_paddle(-STEP)
 