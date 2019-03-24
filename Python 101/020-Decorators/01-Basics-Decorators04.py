# create file 01-Basics-Decorators04.py by using nano 01-Basics-Decorators04.py 

# using a simple decorator for the above case 
# te decorator function exetending the normal functionality of a mysqrt function 
# to print square root of a number
import functools
# the decorator function
def decorator_mysqrt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Please wait...trying to call mysqrt function")
        func(*args, **kwargs)
        print("Thanks...we called mysqrt function")
    return wrapper

# the mysqrt function which will be extended 
@decorator_mysqrt
def mysqrt(num):
    print(num**(1/2))

mysqrt(5)

# now execute the file 
# python 01-Basics-Decorators04.py