# advanced arguments
# we can always give arguments with default value in parametric function
# So we don't always have to input every parameter

# if we want to use unlimited number of arguments in a funtion, we use:
# *args in parameter

# def add(*args):
#     print(args[0]) # this will print 4 here and is a tuple
#     sum = 0
#     for n in args:
#         sum = n + sum
#     return sum
#
# print(add(4,5,7,8,9,10))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)



#     key_word_arguments
#     print(kwargs) # this a data type of dict
#     for key, value in kwargs.items():
#         print(key)
#         print(value)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
# we add get to it, it will return none instead of error, when no input provided
my_car = Car(make="McLaren", model="P1")
print(my_car.make)
print(my_car.model)
