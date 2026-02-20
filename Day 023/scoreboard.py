from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 260)
        self.write_score()
        
        
    def write_score(self):
        self.write(f"Level: {self.current_score}", font=FONT)
        
        
    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write_score()
        
    
    def game_over(self):
        self.goto(0,0)
        self.write("Ouch!\n\n ...Game Over...", align="left", font=FONT)

