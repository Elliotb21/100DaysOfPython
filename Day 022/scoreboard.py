from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 24, "bold")

class Scoreboard(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(position)
        self.write_scoreboard()


    def write_scoreboard(self):
        self.write(f"{self.current_score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write_scoreboard()
   