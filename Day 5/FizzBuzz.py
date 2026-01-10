# Print each number from 1 to 100 inclusive of 100
# If number is divisible by 3, instead of printing the number, print "Fizz"
# If number is divisible by 5, instead of printing the number, print "Buzz"
# If number is divisible by 3 & 5, print "FizzBuzz"

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)