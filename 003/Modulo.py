# Modulo of even numbers is always 0
# Modulo of odd numbers is never 0
# Therefore, it can be determined if a number is odd or even based on modulo 2 of the number.

print(12 % 2) #0
print(11 % 2) #1
print(43927 % 2) #1

print("We will determine via magic if the integer you enter is odd or even.")
number = int(input("Enter your number if you dare...\n"))
if number % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")