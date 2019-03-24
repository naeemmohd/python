# create file 01-Basics-Decorators03.py by using nano 01-Basics-Decorators03.py 

# a function returned from inside other function - but a very cryptic approach
def call_wht(wht,num):
    def mysqrt(num):
        return num**(1/2)
    def mycbrt(num):
        return num**(1/3)
    if wht=='sq':
        return mysqrt
    else:
        return mycbrt
sq = call_wht('sq',5)  # variable sq returns a refrence to the function mysqrt
cb = call_wht('cb',5)  # variable cb returns a refrence to the function mycbrt
print(sq)              # this call will only return that the mysqrt function was called
print(sq(5))           # this call will return the actual value from mysqrt function
print(cb)              # this call will only return that the mycbrt function was called
print(cb(5))           # this call will return the actual value from mycbrt function

# now execute the file 
# python 01-Basics-Decorators03.py