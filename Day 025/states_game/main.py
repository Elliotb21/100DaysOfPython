import turtle
import pandas
import csv

# Screen setup with map
screen = turtle.Screen()
screen.title("United States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Turtle writing object setup
t = turtle.Turtle()
t.penup()
t.hideturtle()

# Get states csv and instantiate variables
states_csv = pandas.read_csv("50_states.csv")
total_guesses = 50
correct_guesses = []


while total_guesses > 1:
    # Prompt for user input
    guess_state = screen.textinput(title= f"{len(correct_guesses)} out of 50!", prompt= "Input a state's name...").title() 
    total_guesses -= 1
    # Exit game if user cancels
    if guess_state == "Exit":
        break  
    # Ignore repeated guesses
    if guess_state in correct_guesses:
        continue  
    # Check if user input matches a known U.S. state
    state_row = states_csv[states_csv["state"] == guess_state]    
    if not state_row.empty:
        x = (state_row["x"].iloc[0])
        y = (state_row["y"].iloc[0])
        t.goto(x, y)
        t.write(arg=guess_state, font=("Arial", 10, "normal"), align="center")
        correct_guesses.append(guess_state)
screen.exitonclick()