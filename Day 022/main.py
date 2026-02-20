from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Initial setup of screen and instantiating pong ball, paddles, scoreboard
screen = Screen()   
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
left_scoreboard = Scoreboard((-100, 250))
right_scoreboard = Scoreboard((100, 250))


screen.listen()
# Paddle movement
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

game_over = False
while not game_over:
    time.sleep(ball.ball_speed)
    screen.update()
  
    # Ball movement and upper wall collisions
    ball.move_ball()  
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # Paddle collision detection and bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # Missed ball and score increment
    elif ball.xcor() > 380:
        ball.reset_ball()
        right_scoreboard.update_score()
        time.sleep(2)
    elif ball.xcor() < -380:
        ball.reset_ball()
        left_scoreboard.update_score()
        time.sleep(2)
        
        
screen.exitonclick()