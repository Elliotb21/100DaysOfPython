import art
print(art.logo)

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

def calculation(num1, num2, operator):
    return (math_dict[operator](num1,num2))
    
def continue_calculating(current_result):
    operator = input("Please enter a mathematical operator (a choice of '+', '-', '*' or '/') ")
    num2 = float(input("Please enter the second number: "))
    current_result = calculation(current_result, num2, operator)
        
num1 = float(input("Please enter the first number: "))
operator = input("Please enter a mathematical operator (a choice of '+', '-', '*' or '/') ")
num2 = float(input("Please enter the second number: "))
current_result = (math_dict[operator](num1,num2))

calculating = True
while calculating:
    continue_flag = input("Do you want to continue operating with the previous result? (y/n): ").lower()
    if continue_flag == "y":
        continue_calculating(current_result)
    else:
        calculation(num1,num2,operator)