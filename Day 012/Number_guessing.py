import random

# This program has the user guess a number between 1 and 100. 
# Easy mode gives 5 guesses and hard mode gives 10 guesses.

countdown = 10
GAME_OVER = False
THE_NUMBER = random.choice(range(0, 101))
print(THE_NUMBER)

def calculate(num):
    """Compares guess to THE_NUMBER. Potentially alters global GAME_OVER variable"""
    global GAME_OVER
    if num == THE_NUMBER:
        print("You guessed it!")
        GAME_OVER = True
    elif num > THE_NUMBER:
        print("Too high")
    elif num < THE_NUMBER:
        print("Too low")


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty 'easy' or 'hard': ").lower()
if difficulty == "easy":
    countdown = 10
elif difficulty == "hard":
    countdown = 5
    
while countdown > 0 and not GAME_OVER:
    guess = int(input(f"You have {countdown} attempts to guess the number, now guess an integer! \n"))
    calculate(guess)
    countdown -= 1