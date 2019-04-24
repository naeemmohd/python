# import custom module to use the User model to create users
from models.usermodel import UserModel

# import safe_str_cmp to safe compare ascii or unicode based strings
from werkzeug.security import safe_str_cmp

# check identity based on payload
def checkIdentity(payload):
    userid= payload['identity']
    return UserModel.getUserById(userid)

# check/authenticate user 
def checkAuthenticity(email, password):
    user = UserModel.getUserByEmail(email)
    if user and safe_str_cmp(user.password, password):
        return user
