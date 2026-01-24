from Menu import MENU, resources
import coffee_functions

# Let's make a coffee machine!

#coffee_functions.report()
machine_on = True
while machine_on:
    user_input = input("Would you like to view 'resources', 'order' a drink, or turn the machine 'off'?\n").lower()
    if user_input == "off":
        machine_on = False
    elif user_input == "resources":
        coffee_functions.report(resources)
    elif user_input == "order":
        ordering = True
        while ordering:    
            user_selection = input("What would you like? (espresso/latte/cappuccino): " ).lower()
            if user_selection in MENU:
                coffee_functions.make_drink(drink_name = user_selection, resources = resources)
            else:
                print("Umm, not sure how to make that... Please try again.")

            should_continue = input("Would you like to order again? ('y' or 'n'): ")
            if should_continue == "n":
                ordering = False
  