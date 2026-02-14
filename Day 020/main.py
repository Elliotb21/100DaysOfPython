from turtle import Turtle, Screen
import time
from snake import Snake

DIFFICULTY = {
    "easy" : 0.2,
    "medium" : 0.1,
    "hard" : 0.07
}

screen = Screen()   
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

snake = Snake()
difficulty_prompt = screen.textinput(title="Select a difficulty", prompt="Easy, Medium, or Hard! ").lower()
if difficulty_prompt:
    game_over = False
while not game_over:
    time.sleep(DIFFICULTY[difficulty_prompt])
    screen.update()
    snake.move()
    
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")    
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")


screen.exitonclick()