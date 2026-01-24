# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  
# It should return True or False.
# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number
# because it is only divisible by 1.
# Example Input 1 = 73 | Example Output 1 = True
# Example Input 2 = 75 | Example Output 2 = False

def is_prime(num):    
    if num in (2,3,5,7,11,13,17,19):
        return True
    if num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    elif num % 4 == 0:
        return False
    elif num % 5 == 0:
        return False
    elif num % 7 == 0:
         return False
    elif num % 9 == 0:
        return False
    else:
        return True
    
print(is_prime(73))
print(is_prime(75))
print(is_prime(19))

# Here is AI's version
def is_prime(num):
    if num <= 1: # 1 or less is not a prime number including all negative numbers.
        return False
    # Calculates square root of the number, then adds one for inclusivity of end number since range() function.
    # e.g. 100 is the num, for integer in range 2 - 11, because sqrt(100)=10, checks against modulo for 2 - 11. 
    # then if condition - if 100 % 2 == 0, then False. The loop performs up until the sqrt + 1, so in the case of num=100, 11.
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False

    return True
