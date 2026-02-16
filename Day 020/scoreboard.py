from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 14, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0    
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.color("white")
        self.write_scoreboard()


    def write_scoreboard(self):
        self.write(f"Score: {self.current_score} ", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write_scoreboard()


    def print_game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!")
