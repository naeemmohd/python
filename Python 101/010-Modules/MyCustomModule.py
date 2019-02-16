# creating a module

from math import pi
def getCustomPI(numberOfDecimals=0):
    return round(pi, numberOfDecimals)

from math import factorial
def getCustomFactorial(num, numberOfDecimals=0):
    return round(factorial(num), numberOfDecimals)