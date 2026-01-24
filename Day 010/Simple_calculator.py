import os
import art

# This is a simple calculator with limited memory

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2
def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2
def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2
def divide(num1, num2):
    """Returns the quotient of two numbers."""
    return num1 / num2

math_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,    
}
# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the fist number again and wipes all memory of previous calculations.

def calculation():
    print(art.logo)
    calculating = True
    num1 = float(input("Please enter the first number: "))
    
    while calculating:    
        for operator in math_dict:
            print(operator)
        operator = input("Please enter a mathematical operator: ")
        num2 = float(input("Please enter the second number: "))
        answer = (math_dict[operator](num1,num2))
        print(f"{num1} {operator} {num2} = {answer}")
        choice = input(f"Do you want to continue operating with {answer}? (y/n): ").lower()
        if choice == "y":
            num1 = answer
        else:
            calculating = False
            print(os.system('cls' if os.name == "nt" else 'clear'))
            calculation()
calculation()