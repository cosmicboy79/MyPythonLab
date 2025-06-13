"""
Using the @logme decorator.
"""
from logging.mylog import logme, Level


@logme
def add(a, b):
    return a + b


@logme(level=Level.INFO)
def subtract(a, b):
    return a - b


@logme(level=Level.DEBUG)
def multiply(a, b):
    return a * b


@logme
def divide(a, b):
    return a / b


print("Adding two numbers: " + str(add(1, 2)))
print("Subtracting two numbers: " + str(subtract(8, 3)))
print("Multiplying two numbers: " + str(multiply(5, 6)))
print("Dividing two numbers: " + str(divide(45, 5)))
