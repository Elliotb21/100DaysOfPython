def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    
# Function1 basically echos the text
def function1(text):
    result = text + " " + text
    return result
# Function2 makes the words title case
def function2(text):
    transform = text.title()
    return transform
print(function2(function1("This is a test")))
print("\n")
output = function2(function1("HeLlO"))
print(output)
