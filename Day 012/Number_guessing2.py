# This is the walkthrough version

from random import randint

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def set_difficulty():
    """Sets game difficulty."""
    difficulty = input("Select a difficulty: 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_DIFFICULTY
    elif difficulty == "hard":
        return HARD_DIFFICULTY

def check_answer(user_guess, actual_answer, turns):
    """Logic for comparing guess & answer. Returns turn decrement by 1 if guess != answer"""
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You guessed it! The answer was {actual_answer}")

def game():
    answer = randint(1,100)
    print("Welcome the number guessing game!")
    print("I'm thinking of a number between 1 and 100...")
    turns = set_difficulty()
    guess = 0
    while guess != answer and turns > 0:
        print(f"You have {turns} remaining to guess. ")
        guess = int(input("Guess an integer: "))
        turns = check_answer(guess, answer, turns)
game()