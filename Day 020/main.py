from turtle import Screen
import time
from snake import Snake
from food import Food

# Modifies the speed of screen updates
DIFFICULTY = {
    "easy" : 0.2,
    "medium" : 0.1,
    "hard" : 0.07
}

# Initial setup of screen and instantiating snake and food objects
screen = Screen()   
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)
snake = Snake()
food = Food()

# Queries user for difficulty. Main game section
difficulty_prompt = screen.textinput(
    title="Select a difficulty", 
    prompt="Easy, Medium, or Hard! "
)

if difficulty_prompt:
    difficulty_prompt = difficulty_prompt.lower()
difficulty = DIFFICULTY.get(difficulty_prompt, DIFFICULTY["medium"])

# Listen for screen events, and match snake movement to arrow keys.
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")    
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_over = False
while not game_over:
    time.sleep(difficulty)
    screen.update()
    snake.move()
    
    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
    
  


screen.exitonclick()    