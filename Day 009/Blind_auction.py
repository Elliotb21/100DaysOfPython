import os
from art import logo, prize
print(logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

auction = {}
bidding = True

def find_highest_bid(bids_dictionary):
    # highest_bid = 0
    # winner = ""
    winner = max(bids_dictionary, key=bids_dictionary.get) # Built in method far quicker and easier than creating loop
    highest_bid = bids_dictionary[winner]
    # for bidder in bids_dictionary:
    #     if bids_dictionary[bidder] > highest_bid:
    #         highest_bid = bids_dictionary[bidder]
    #         winner = bidder
    return winner, highest_bid

while bidding:
    name = input("Please enter your name: ").capitalize()
    bid = int(input("Please enter your bid: $"))
    auction[name] = bid
    
    continue_bidding = input("Are there more bidders? (y/n): ").lower()
    if continue_bidding == "y":
        os.system('cls' if os.name == 'nt' else 'clear') # AI assist
    else:
        print(prize)
        winner, highest_bid = find_highest_bid(auction)
        print(f"The winner is {winner} with a bid of ${highest_bid}\n\n") 
        bidding = False
