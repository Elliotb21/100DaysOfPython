# def add(*args):
#     return sum(args)
# print(add(2,2,3))

def subtract(*args):
    difference = args[0]
    for item in args[1:]:
        difference -= item
    return difference
print(subtract(1,2,3,4,5))
