# This is the version that Angela Yu helps walk students through. 
# I am making it for muscle memory and to improve on my version. Though it's working, it is poorly optimized.

from art import logo
import random
import os

def deal_card():
    """Returns a single, random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards, and return the score from the list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    return sum(cards)

def compare(u_score, d_score):
    """Compares the user score against the dealer score."""
    if u_score == d_score:
        return "Tie game!"
    elif u_score == 0:
        return "Blackjack! You win!"
    elif d_score == 0:
        return "Blackjack! You lose!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif d_score > 21:
        return "Dealer went over. You win!"
    elif u_score > d_score:
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    user_score = -1
    dealer_score = -1
    game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your hand {user_cards} = {user_score}")
        print(f"Dealer hand {dealer_cards[0]}")
        
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else: 
                game_over = True
    
    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        
    print(f"Your hand was: {user_cards} = {user_score}")
    print(f"Dealer hand was: {dealer_cards} = {dealer_score}")
    print(compare(user_score, dealer_score))
    
while input("Do you want to play a game of BlackJack? (y/n): ").lower() == "y":
    "cls" if os.system == "nt" else "clear"
    play_game()