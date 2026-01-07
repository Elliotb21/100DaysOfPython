import RPS_AsciiArt
import random

# This game pits a user against the computer in the classic game of rock, paper, scissors!
RPS = ["Rock", "Paper", "Scissors"]

# User 
print("What do you choose? ")
user_choice = input("[R]ock, [P]aper, or [S]cissors? ").lower()
if user_choice == "r":
    print("You chose rock.")
    print(RPS_AsciiArt.rock)
elif user_choice == "p":
    print("You chose paper")
    print(RPS_AsciiArt.paper)
elif user_choice == "s":
    print("You chose scissors")
    print(RPS_AsciiArt.scissors)
else:
    print("That is not a valid selection. Please choose 'R', 'P', or 'S' ")

# Computer
computer_choice = random.choice(RPS)
print(f"The computer chose {computer_choice}")
if computer_choice == "Rock":
    print(RPS_AsciiArt.rock)
elif computer_choice == "Paper":
    print(RPS_AsciiArt.paper)
else:
    print(RPS_AsciiArt.scissors)


# Determination
print("\n\n")
if user_choice == "r" and computer_choice == "Scissors":
    print("User wins!")
    print(RPS_AsciiArt.user_wins)
elif user_choice == "r" and computer_choice == "Paper":
    print("Computer wins!")
    print(RPS_AsciiArt.computer_wins)
elif user_choice == "r" and computer_choice == "Rock":
    print("Tie game!")

if user_choice == "p" and computer_choice == "Rock":
    print("User Wins!")
    print(RPS_AsciiArt.user_wins)
elif user_choice == "p" and computer_choice == "Scissors":
    print("Computer wins!")
    print(RPS_AsciiArt.computer_wins)
elif user_choice == "p" and computer_choice == "Paper":
    print("Tie game!")
    
if user_choice == "s" and computer_choice == "Paper":
    print("User wins!")
    print(RPS_AsciiArt.user_wins)
elif user_choice == "s" and computer_choice == "Rock":
    print("Computer wins!")
    print(RPS_AsciiArt.computer_wins)
elif user_choice == "s" and computer_choice == "Scissors":
    print("Tie game!")