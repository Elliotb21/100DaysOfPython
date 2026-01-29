from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

CoffeeMaker = CoffeeMaker()
Menu = Menu()
Money = MoneyMachine()

machine_on = True
while machine_on:
    user_selection = input("Would you like to view 'resources', 'order' a drink, or turn the machine 'off'? ")
    if user_selection == "off":
        machine_on = False
    elif user_selection == "resources":
        print(CoffeeMaker.report())
    elif user_selection == "order":
        order = input(f"What would you like to order: {Menu.get_items()} ? \n")
        drink = Menu.find_drink(order)
        if CoffeeMaker.is_resource_sufficient(drink):
                CoffeeMaker.make_coffee(drink)
        
    else:
        print("That was not a valid selection.")