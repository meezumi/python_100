# Python Decorator Function
import time
def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        # do something before
        function()
        # do something after
    return wrapper_function

# decorator function is just a function that wraps another function
# and gives that function some additional functionality.

# if we want to aaa a delay of 2 to each of the below functions,
# we can simply use decorator_function

@decorator_function
def say_hello():
    print("hello")
# or decorated = decorator_function(say_hello)
# decorated()


@decorator_function
def say_bye():
    print("bye")


def say_greeting():
    print("how you doing?")

# @decorator_function is a syntactic sugar


