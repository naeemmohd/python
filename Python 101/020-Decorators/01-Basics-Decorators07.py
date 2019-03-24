# create file 01-Basics-Decorators07.py by using nano 01-Basics-Decorators07.py 

# using a simple decorator but now decorating it debug the method as well as to find how much time it took to process
import functools
import time
# the decorator function
def decorator_mysqrt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Please wait...trying to call mysqrt function on list")
        argsstr = [repr(a) for a in args]                      
        kwargsstr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        methodsignature = ", ".join(argsstr + kwargsstr)           
        print(f"Calling {func.__name__}({methodsignature})")
        starttime = time.perf_counter() 
        time.sleep(1)
        print("Just sleeping for few secs to have some fun")
        
        retvalue = func(*args, **kwargs)
        
        endtime = time.perf_counter() 
        totaltime = starttime - endtime
        print(f"Finished the function {func.__name__!r} in {totaltime:.4f} secs with return value {retvalue!r}.")
        return retvalue
    return wrapper

# the mysqrt function which will be extended 
@decorator_mysqrt
def mysqrt(nums):
    retList ={}
    for num in nums:
        retList.update({num:num**(1/2)})
    return retList

mylist =[x for x in range(1,6)]
mysqrt(mylist)

# now execute the file 
# python 01-Basics-Decorators07.py