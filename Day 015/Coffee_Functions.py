# Functions for the coffee machine found in main.py
from Menu import MENU, resources
from decimal import Decimal

def report(resources):
    """Shows the current resource values."""
    print(f"Water = {resources['water']} \nMilk = {resources['milk']} \nCoffee = {resources['coffee']} \nMoney = ${resources['money']:.2f}") 
    
    
def make_drink(drink_name, resources):
    drink = MENU[drink_name]["ingredients"]
    cost = Decimal(str(MENU[drink_name]["cost"]))
    
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return
        
    print(f"The cost for {drink_name} is ${cost:.2f}")
    payment = insert_money()
    sufficient_payment = calculate(cost, payment)
    
    if sufficient_payment:
        for ingredient in drink:
            resources[ingredient] -= drink[ingredient]
        print(f"Here is your {drink_name}! ☕")
 
 
def insert_money():
    """Queries for coin payment. Returns payment as a decimal total."""
    payment = int(input("Please insert quarters: ")) * Decimal("0.25")
    payment += int(input("Please insert dimes: ")) * Decimal("0.10")
    payment += int(input("Please insert nickels: ")) * Decimal("0.05")
    payment += int(input("Please insert pennies: ")) * Decimal("0.01")
    return payment

                     
def calculate(drink_cost, payment_total):
    """Compares payment entered from insert_money to drink cost and returns Boolean."""
    drink_cost = Decimal(str(drink_cost))
    if drink_cost > payment_total:
        print(f"""That's not enough money...You put in ${payment_total:.2f} and the drink costs ${drink_cost}.
              Please take your money.""")
        return False
    elif drink_cost == payment_total:
        resources["money"] += drink_cost
        return True
    else:
        refund = payment_total - drink_cost
        print(f"Refund: ${refund:.2f}")
        resources["money"] += drink_cost
        return True

