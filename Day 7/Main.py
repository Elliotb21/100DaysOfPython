import random
from HangmanWords import word_list
from HangmanArt import stages, logo

# Hangman the game!

# Print the logo, pick a word, print the word, and give a hint to the user.
print(logo)
print(stages[-1])
chosen_word = random.choice(word_list)
dashes = "-" * len(chosen_word)
print(f"Your word to guess is: {len(chosen_word)} letters long.\n   {dashes} ")
    
correct_letters = []
lives = 6
game_over = False
while not game_over:
    displayed_word = ""
    guess = input("\nGuess a letter: ")
    
    if guess in correct_letters:
        print(f"You've already guessed the letter: {guess}")
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the answer...")
        lives -= 1
        
    for letter in chosen_word:
        if letter == guess:
            displayed_word += guess
            correct_letters.append(letter)         
        elif letter in correct_letters:
            displayed_word += letter  
        else:
            displayed_word += "_"
    print(displayed_word)

    if lives >= 1:
        print(stages[lives])
        print(f"You have {lives} live(s) left!")
    else:    
        print("You lose!")
        print(f"The word was: {chosen_word}")
        print(stages[lives])
        game_over = True
    if "_" not in displayed_word:
        game_over = True
        print("You won!")