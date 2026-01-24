# Higher or lower is a game where you choose which item has more popularity. 
from random import randint
from Game_Data import DATA
import art
import os

game_over = False
high_score = 0

def compare(choice, count_to_compare):
    if choice > count_to_compare:
        print("You got it!")
        return high_score + 1, False
    else:
        print("Oh no! You guessed wrong. Clearly you know nothing.")
        return high_score, True
print(art.logo)
dict_2 = DATA[randint(0, len(DATA)-1)]

while not game_over:     
    dict_1 = dict_2
    dict_2 = DATA[randint(0, len(DATA)-1)]
    if dict_1 == dict_2:
        dict_2 = DATA[randint(p, len(DATA)-1)]
    print(f"Compare A:  {dict_1["name"]}, a(n) {dict_1["description"]}, from {dict_1["country"]}.")
    print(art.vs)
    print(f"With B:  {dict_2["name"]}, a(n) {dict_2["description"]}, from {dict_2["country"]}.")
    a_count = dict_1["follower_count"]
    b_count = dict_2["follower_count"]
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(art.logo)
    os.system('cls' if os.name == "nt" else 'clear')
    if user_choice == 'a':
        user_choice = a_count
        comparison_count = b_count
    else:
        user_choice = b_count
        comparison_count = a_count
    high_score, game_over = compare(user_choice, comparison_count)
    print(f"Your high score is: {high_score}")


        