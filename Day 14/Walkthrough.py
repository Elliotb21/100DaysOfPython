from art import logo, vs
from Game_Data import DATA
import random

print(logo)

def format_data(account):
    """Takes the account data and returns a printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"
    
def check_answer(user_guess, a_followers, b_followers):
    """Takes the user guess and the follower counts, returns if they got it right."""
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
score = 0
game_over = False
account_b = random.choice(DATA)

while not game_over:   
    # Generate a random account
    account_a = account_b
    account_b = random.choice(DATA)
    if account_a == account_b:
        account_b = random.choice(DATA)

        
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    #Ask the user for a guess.
    guess = input("Who has more followers, type 'A' or 'B': ").lower()
    is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])
    if is_correct:
        score += 1
        print(f"You got it! Your score is currently: {score}.")
    else:
        print(f"That's wrong. Your final score was: {score}.")
        game_over = True