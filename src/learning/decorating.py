"""
Decorators receive a function to be executed when it is called.
However, some other action can be done before or after its execution.
The idea is to encapsulate some behaviour that should happen on top of
some operation and can be reused everywhere it is needed.
"""
from functools import wraps

def log_function(func):
    @wraps(func) # this ensures docstring, function name, arguments list, etc. are all copied
                 # to the wrapped function - instead of being replaced with wrapper's info
    def wrapper(*args, **kwargs):
        print("Entering function {}".format(func.__name__))
        result = func(*args, **kwargs)
        print("Exiting function {}".format(func.__name__))
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

@log_function
def subtract(a, b):
    return a - b

@log_function
def multiply(a, b):
    return a * b

@log_function
def divide(a, b):
    return a / b

print("Adding two numbers: " + str(add(1, 2)))
print("Subtracting two numbers: " + str(subtract(8, 3)))
print("Multiplying two numbers: " + str(multiply(5, 6)))
print("Dividing two numbers: " + str(divide(45, 5)))
