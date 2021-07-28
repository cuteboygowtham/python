import sys


def tempf2c(t):
    fahrenheit = float(t)
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def tempc2f(t):
    celsius = float(t)
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


x = float(input("Enter Ur Fahrenheit value"))
temperature = tempf2c(x)
print(temperature)
y = float(input("enter ur celsius value"))
temp = tempc2f(y)
print(temp)
