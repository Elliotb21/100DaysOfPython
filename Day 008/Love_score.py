# Love Calculator
# This is a difficult challenge! 
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  
# To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53


true_list = ['t', 'r', 'u', 'e']
love_list = ['l', 'o', 'v', 'e']

def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    combined_names = (name1 + name2).lower()

    for letter in combined_names:
        if letter in true_list:
            true_count += 1
        
    for letter in combined_names:
        if letter in love_list:
            love_count += 1
    # Below could replace line 31 - 37 and is more Pythonic.
    # true_count = sum(combined_names.count(letter) for letter in "true")
    # love_count = sum(combined_names.count(letter) for letter in "love")
    print(true_count, love_count, sep="")

calculate_love_score("Ingrid Bond","Elliot Bond")