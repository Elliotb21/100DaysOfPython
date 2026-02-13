from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

snake = Snake()


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)     
      
    snake.move()


screen.exitonclick()