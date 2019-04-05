# import custom module to use the User model to create users
from usermodel_v2 import User

# import safe_str_cmp to safe compare ascii or unicode based strings
from werkzeug.security import safe_str_cmp

# create users
users = [
    User(1,"Naeemm@futurecloud.com", "PassNaeem"),
    User(2, "Test02@futurecloud.com", "PassTest02"),
    User(3, "Test03@futurecloud.com", "PassTest03")
]

# a dictionary for user names
userEmails = {user.email : user for user in users}
# a dictionary for user ids
userIds = {user.id : user for user in users}

# check identity based on payload
def checkIdentity(payload):
    userid= payload['identity']
    return userIds.get(userid, None)

# check/authenticate user 
def checkAuthenticity(email, password):
    user = userEmails.get(email, None)
    if user and safe_str_cmp(user.password, password):
        return user