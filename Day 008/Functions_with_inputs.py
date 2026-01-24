# Demonstrating passing parameters to a function and then passing arguments to the function call.

def greet():
    print("Hello.")
    print("How are you?")
    print("I am fine, thank you.")
#greet()

def greet_with_name(name):
    print(f"Hello, {name}")
    print("How are you?")
    print(f"I am fine {name}, thank you.")
    
#greet_with_name("Joe")
#greet_with_name("Bob")

def greet_with(name,location):
    print(f"Hey, {name}")
    print(f"I see you're from {location}")
    print("What is the weather like there?")

greet_with("Bob", "United States")
greet_with(location = "United States", name = "Bob")
# Positional argument vs named arguments provide continuity when order is not maintained.