from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0    
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.color("white")
        self.write(f"Score: {self.current_score} ", False, align="center", font=("Courier New", 14, "normal"))


    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score: {self.current_score} ", False, align="center", font=("Courier New", 14, "normal"))

