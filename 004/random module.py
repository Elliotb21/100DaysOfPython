import random
from my_favorite_number import number

random_between_0_and_1 = random.uniform(0,number)
random_integer = random.randint(1,1000)
random_value = random.randrange(0,10,2)

print(random_between_0_and_1)
print(random_integer)
print(random_value)
