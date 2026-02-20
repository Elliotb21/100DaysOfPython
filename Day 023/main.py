import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup and player object instantiated. Cars list created for iteration.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
cars = []
# Player controls
screen.listen()
screen.onkey(player.move, "Up")
# Spawn condition instantiation
counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Spawn condition update
    counter += 1
    # Generate cars
    if counter % 6 == 0:
        car = CarManager()
        cars.append(car)
    # Move cars across screen
    for car in cars:
        car.move()
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False
    if player.safely_crossed():
        player.reset()
        scoreboard.update_score()
        car.next_level()
            
        
    
    
screen.exitonclick()