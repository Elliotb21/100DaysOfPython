# Starting code
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(15)
# First step is to see what the program actually does and compare it to what we want it to do.
# Using a target of 10, and viewing the output, it appears 3 triggers FizzBuzz, but 3 is only divisible by 3, not 3 and 5.
# This gives us somewhere to look - the first comparison evaluates to True because it is using an OR statement.
# Changing the comparison on line 5 to AND gives us progress. Repeating the runtime we see that 5 prints Buzz, then Fizz.

# Second step, on [6], using debugger, we can see the final if statement is tied to an else statement, and so a previous if
# and the final else statement both trigger, when only one should.

# Third step, on a value that FizzBuzz should be executed (15) we can see that multiple if statements are occurring, when
# it should be if, elif, else, rather than checking every condition every time.

# Fourth step, I guess they don't want the index printed, just the number, so we remove the square brackets on line 12
# ([number])