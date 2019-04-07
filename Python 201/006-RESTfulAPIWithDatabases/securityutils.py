# import custom module to use the User model to create users
from userDAL import User

# import safe_str_cmp to safe compare ascii or unicode based strings
from werkzeug.security import safe_str_cmp

# check identity based on payload
def checkIdentity(payload):
    userid= payload['identity']
    return User.getUserById(userid)

# check/authenticate user 
def checkAuthenticity(email, password):
    user = User.getUserByEmail(email)
    if user and safe_str_cmp(user.password, password):
        return user
