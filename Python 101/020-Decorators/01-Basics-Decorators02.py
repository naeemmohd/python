# create file 01-Basics-Decorators02.py by using nano 01-Basics-Decorators02.py 

# a function called inside other function
def call_all(num):
    def mysqrt(num):
        return num**(1/2)
    def mycbrt(num):
        return num**(1/3)
    sqrt = mysqrt(num)
    print(sqrt)
    cbrt = mycbrt(num)
    print(cbrt)
call_all(5)

# now execute the file 
# python 01-Basics-Decorators02.py