def add(*args):
    return sum(args)
print(add(2,2,3))

def subtract(*args):
    sum = args[0]
    for item in range(args[1]):
        sum -= item
    return sum
print(subtract(5,3))
