import os
from Menu import MENU, resources
import Coffee_Functions

# Let's make a coffee machine!

#Coffee_Functions.report()
machine_on = True
while machine_on:
    user_input = input("Would you like to view resources, order a drink, or turn the machine off? ").lower()
    if user_input == "resources":
        Coffee_Functions.report(resources)
    elif user_input == "off":
        machine_on = False
    elif user_input == "order":
        ordering = True
        while ordering:        
            user_selection = input("What would you like? (espresso/latte/cappuccino): " ).lower()

            if user_selection == "espresso":
                Coffee_Functions.espresso(resources)
            elif user_selection == "latte":
                Coffee_Functions.latte(resources)
            elif user_selection == "cappuccino":
                Coffee_Functions.cappuccino(resources)
            else:
                print("Umm, not sure how to make that... Please try again. ")
            should_continue = input("Would you like to order again? ('y' or 'n'): ")
            if should_continue == "n":
                ordering = False
    
    