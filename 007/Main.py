import random

# Hangman the game!

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Choose a letter from the alphabet! ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        
#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    
    #Check if user is wrong.
    
#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

    #Join all the elements in the list and turn it into a String.

    #Check if user has got all letters.

#TODO-6: - Import the stages from hangman_art.py and make this error go away.
