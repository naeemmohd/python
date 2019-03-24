# create file 01-Basics-Decorators06.py by using nano 01-Basics-Decorators06.py 

## logic to let a user go to admin page if he was an admin user lets use decorators
# decorators with passing arguments
# the decorator function
import functools
def decorator_adminaccess(role):
    def decorator_adminaccess(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Please wait...while we are checking your credentia;ls function")
            if role == 'admin':
                func(*args, **kwargs)
            else:
                print("Sorry...you dont have access. Please check with the admin")
        return wrapper
    return decorator_adminaccess

# the adminaccess function which will be extended - its a very simple function which greets and takes you to admin console
@decorator_adminaccess('admin')      # decorator with a parameter
def adminaccess(name):
    print("Welcome {} you got access. We are redirecting you to admin console".format(name))

print(adminaccess('Naeem'))

# now execute the file 
# python 01-Basics-Decorators06.py