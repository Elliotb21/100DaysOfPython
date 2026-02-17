from turtle import Turtle, Screen
import time
from paddles import Paddle

PADDLE1_START_POSITION = (-370, 0)
PADDLE2_START_POSITION = (370, 0)

# Initial setup of screen and instantiating pong ball, paddles, scoreboard
screen = Screen()   
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
# screen.tracer(0)
Paddle_1 = Paddle(PADDLE1_START_POSITION)
Paddle_2 = Paddle(PADDLE2_START_POSITION)


screen.exitonclick()