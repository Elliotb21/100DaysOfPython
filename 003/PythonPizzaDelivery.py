# This program calculates the price of a pizza with or without modifiers such as pepperoni.
# Small = $15, Medium = $ 20, Large = $25
# Pepperoni is $3 extra, except on small it is only $2 extra
# Cheese is always $1 extra

print("Welcome to the Python Pizza Parlour\nPlease place your order.")
total = 0
size = input("You may order [S]mall, [M]edium, or [L]arge ")
pepperoni = input("Would you like pepperoni? (Y or N)")
cheese = input("Would you like extra cheese? (Y or N) ")

if size == "S":
    total = 15
    if pepperoni == "Y":
        total += 2
    if cheese == "Y":
        total += 1
elif size == "M":
    total = 20
    if pepperoni == "Y":
        total += 3
    if cheese == "Y":
        total += 1
elif size == "L":
    total = 25
    if pepperoni == "Y":
        total += 3
    if cheese == "Y":
        total += 1
else:
    print("There was a problem with your entry...")
print(f"Your total is: ${total}")

#Here's what I came up with, and below is what Chat GPT suggested:

#print("Welcome to the Python Pizza Parlour\nPlease place your order.")
#size = input("You may order [S]mall, [M]edium, or [L]arge ")
#pepperoni = input("Would you like pepperoni? (Y or N)")
#cheese = input("Would you like extra cheese? (Y or N) ")

#prices = {"S": 15, "M": 20, "L": 25}

#if size in prices:
#    total = prices[size]
#    if pepperoni == "Y":
#        total += 2 if size == "S" else 3
#    if cheese == "Y":
#        total += 1
#    print(f"Your total is: ${total}")
#else:
#    print("There was a problem with your entry...")
