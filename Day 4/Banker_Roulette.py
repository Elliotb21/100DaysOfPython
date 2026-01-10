# The goal of this program is to randomly pick a name out of a list.

import random
names = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

random_selection = random.randint(0,4)
print(names[random_selection])

print(random.choice(names))
