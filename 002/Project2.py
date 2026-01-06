print(type("Hello"))    #String
print(type(123))        #Integer
print(type(False))      #Boolean
print(type(123_456.789))#Float with underscore in lieu of comma for readability

#Typecasting in Python is type conversion from string to integer in this case
print("123" + "456")
print(int("123") + int("456"))      

#ValueError in Python indicates invalid literal for argument
#print(int("abc") + int("123"))

#Original Code
#print("Number of letters in your name: " + len(input("Enter your name:")))

#Solution
name_length = input("Enter your name: ")
print("There are " + str(len(name_length)) + " letters in your name")