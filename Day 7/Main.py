import random
from HangmanWords import word_list
from HangmanArt import stages,logo

# Hangman the game!
print(logo)

chosen_word = random.choice(word_list)
dashes = "-" * len(chosen_word)
print(f"Your word to guess is: {len(chosen_word)} letters long.\n   {dashes} ")



guessed_word_list = []
index_number = 0
for letter in chosen_word:
    guessed_word_list += "-"
    if letter == guess:
        guessed_word_list[index_number] = guess
    elif letter == guessed_word_list[index_number]:
        print("You already guessed that letter.")
    else:
        print("That guess was wrong!")
    index_number += 1

guessed_word = ""
for value in guessed_word_list:
    guessed_word += value
print(guessed_word)

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    
    #Check if user is wrong.
    
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

    #Join all the elements in the list and turn it into a String.

    #Check if user has got all letters.

#TODO-6: - Import the stages from hangman_art.py and make this error go away.
