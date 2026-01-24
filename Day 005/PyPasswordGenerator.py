import random

# Simple Python password generator!
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
holder = []

# Prompt
print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters should be in the password? "))
num_symbols = int(input("How many symbols should be in the password? "))
num_numbers = int(input("How many numbers should be in the password? "))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if num_letters > 0:
    for num in range(num_letters):
        password += random.choice(letters)
if num_symbols > 0:
    for num in range(num_symbols):
        password += random.choice(symbols)
if num_numbers > 0:
    for num in range(num_numbers):
        password += random.choice(numbers)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# For a character in the already populated password, append to a list named holder. Then shuffle in place
for char in password:
    holder.append(char)
random.shuffle(holder)

# Reset the password value because it is held in the variable holder as a list. Then iterate through each character
# and add it to the end of the password string. 
password = ""
for char in holder:
    password += char
print(password)