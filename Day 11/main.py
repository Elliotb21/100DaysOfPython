from art import logo
import random
import os

# Our Blackjack Game House Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []

def calculate_totals():
    """Calculates both hands of cards. Returns the totals of each hand."""
    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)
    return player_total, dealer_total

def initial_deal():
    """Deals two cards and shows the starting hands to user. Returns the totals of each hand."""
    for hand in (player_hand, dealer_hand):
        hand.clear()
    for card in range(2):
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
    player_total, dealer_total = calculate_totals()
    print(f"Dealer's hand: [{dealer_hand[0]}, hidden]")
    print(f"Player's hand: {player_hand} = {player_total}")
    return player_total, dealer_total

def change_ace(player_total, dealer_total):
    """If over 21 and has an Ace, changes the Ace to a 1. Returns the totals of each hand."""
    while 11 in player_hand and player_total > 21:
        ace = player_hand.index(11)
        player_hand[ace] = 1
        player_total, dealer_total = calculate_totals()
            
    while 11 in dealer_hand and dealer_total > 21:
        ace = dealer_hand.index(11)
        dealer_hand[ace] = 1
        player_total, dealer_total = calculate_totals()
    return calculate_totals()

def player_hit(player_total):
    """Deals a card to the player. Shows their hand at the end, and returns the player_total"""
    if player_total == 21:
        print("You are at 21.")
    else:
        player_hand.append(random.choice(cards))
        player_total, dealer_total = calculate_totals()
        player_total, dealer_total = change_ace(player_total, dealer_total)      
    print(f"Player's hand: {player_hand} = {player_total}")
    return player_total

   
def dealer_hit(dealer_total):
    """Deals a card to the dealer if under 17, changes the Ace if they've gone over, and returns the dealer_total"""
    while dealer_total < 17:
        dealer_hand.append(random.choice(cards))
        player_total, dealer_total = calculate_totals()
        change_ace(player_total, dealer_total)
    return dealer_total
    
def calculate_winner(player_total, dealer_total):
    """Game logic for who wins."""
    if player_total == dealer_total:
        print(f"Dealer's current hand is: {dealer_hand} = {dealer_total}")
        print(f"Player's current hand is: {player_hand} = {player_total}")
        print("Tie game.")
    elif player_total > dealer_total:
        print(f"Dealer's current hand is: {dealer_hand} = {dealer_total}")
        print(f"Player's current hand is: {player_hand} = {player_total}")
        print("You win!")
    else:
        print(f"Dealer's current hand is: {dealer_hand} = {dealer_total}")
        print(f"Player's current hand is: {player_hand} = {player_total}")
        print("Dealer wins!")
     
keep_playing = True
while keep_playing:
    wants_to_play = input("Do you want to play a game of BlackJack? (y/n): ").lower()  
    if wants_to_play == "y":
        os.system('cls' if os.name == "nt" else 'clear')
        print(logo)
        player_total, dealer_total = initial_deal()
        if player_total == 22 or dealer_total == 22:
            change_ace(player_total, dealer_total)
            player_total, dealer_total = calculate_totals()       
            
        while player_total <= 21:
            hit_or_stay = input("Type 'hit' or 'stay': ").lower()
            if hit_or_stay == "hit":
                player_total = player_hit(player_total)
                player_total, dealer_total = calculate_totals()
            elif hit_or_stay == "stay":
                player_total, dealer_total = calculate_totals()
                print(f"Dealer's turn to play.")
                dealer_total = dealer_hit(dealer_total)
                break
            else:
                print("Your input was invalid. Type 'hit' or 'stay'... ")       
        if player_total > 21: 
            print("You went over. Dealer wins automatically.")   
            print(f"Dealer's current hand is: {dealer_hand} = {dealer_total}")
            print(f"Player's current hand is: {player_hand} = {player_total}")
        elif dealer_total > 21:  
            print("Dealer went over. Player wins!")
            print(f"Dealer's current hand is: {dealer_hand} = {dealer_total}")
            print(f"Player's current hand is: {player_hand} = {player_total}")
        else:
            calculate_winner(player_total, dealer_total)
    else:
        keep_playing = False
