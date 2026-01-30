from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    user_selection = input("Would you like to view 'resources', 'order' a drink, or turn the machine 'off'? ")
    if user_selection == "off":
        machine_on = False
    elif user_selection == "resources":
        coffee_maker.report()
        money_machine.report()
    elif user_selection == "order":
        order = input(f"What would you like to order: {menu.get_items()} ? \n")
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)        
    else:
        print("That was not a valid selection.")
        
        