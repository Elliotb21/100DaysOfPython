#This demonstrates if/then statements, nested if/then, and multi-conditional statements

print("Welcome to the rollercoaster")
height = int(input("What is your height in inches? "))

if height >= 48:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Ticket price is $5")
        total = 5
    elif age <= 18:
        print("Ticket price is $7")
        total = 7
    else:
        print("Ticket price is $10")
        total = 10
        
    photo = input("Do you want a photo for $5? (y/n) ")
    if photo == "y":
        total = total + 5
    print(f"The total price is - ${total}")
else:
    print("You are not tall enough to ride.")
    