# def add(*args):
#     return sum(args)
# print(add(2,2,3))

# def subtract(*args):
#     difference = args[0]
#     for item in args[1:]:
#         difference -= item
#     return difference
# print(subtract(1,2,3,4,5))


# def calculate(num, **kwargs):
    # for key, value in kwargs.items():
    #     print(key, value)
    # print(type(kwargs))    
    # print(kwargs)
    # print(kwargs["add"]) num + '5' is 10
    # num *= kwargs["multiply"] num * '2' is 20
    # return num
    
# print(calculate(5, add=5, multiply=2))

class Car():
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.color = kwargs.get("color") #The benefit of get is that it will return none so it won't crash 
                                         #if no value is passed
        
my_car = Car(make="Honda", model="Civic")
print(my_car.make)
print(my_car.color)

import tkinter

window = tkinter.Tk()
window.mainloop()
