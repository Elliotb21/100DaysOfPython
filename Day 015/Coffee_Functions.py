# Functions for the coffee machine found in main.py
from Menu import MENU, resources


def report(resources):
    """Shows the current resource values."""
    print(f"Water = {resources["water"]} \nMilk = {resources["milk"]} \nCoffee = {resources["coffee"]} \n") 
    
def espresso(resources):
    drink = MENU["espresso"]["ingredients"]
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return
        
    for ingredient in drink:
        resources[ingredient] -= drink[ingredient]
    print("Here is your espresso! ☕")

def latte(resources):
    drink = MENU["latte"]["ingredients"]
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return
    for ingredient in drink:
        resources[ingredient] -= drink[ingredient]
    print("Here is your latte! ☕")

    
def cappuccino(resources):
    drink = MENU["cappuccino"]["ingredients"]
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return
    
    for ingredient in drink:
        resources[ingredient] -= drink[ingredient]
    print("Here is your cappuccino! ☕")

    