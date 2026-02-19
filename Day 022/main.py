from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball


# Initial setup of screen and instantiating pong ball, paddles, scoreboard
screen = Screen()   
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)
Paddle_R = Paddle((350,0))
Paddle_L = Paddle((-350,0))
ball = Ball()

screen.listen()
# Paddle movement
screen.onkey(Paddle_R.paddle_up, "Up")
screen.onkey(Paddle_R.paddle_down, "Down")
screen.onkey(Paddle_L.paddle_up, "w")
screen.onkey(Paddle_L.paddle_down, "s")

game_over = False
while not game_over:
    time.sleep(0.03)
    screen.update()
  
    # Ball movement and wall collisions
    ball.move_ball()  
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

screen.exitonclick()