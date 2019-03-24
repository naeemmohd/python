# create file 01-Basics-Decorators05.py by using nano 01-Basics-Decorators05.py 

# using a simple decorator for the above case  but with the function returning a return value
# te decorator function exetending the normal functionality of a mysqrt function 
# to print square root of a number
import functools
# the decorator function
def decorator_mysqrt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Please wait...trying to call mysqrt function")
        retvalue = func(*args, **kwargs)
        return retvalue  # this must be there for the function to a return value
        print("Thanks...we called mysqrt function") # but this will not be called because you are returning before it
    return wrapper

# the mysqrt function which will be extended 
@decorator_mysqrt
def mysqrt(num):
    #print(num**(1/2))
    return num**(1/2)  # now you can return a  instead of print value

print(mysqrt(5))

# now execute the file 
# python 01-Basics-Decorators05.py