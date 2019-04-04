#create a User model class to represent a user and its credentials
class User(object):
    def __init__(self, _id, username, password):
        self.id= _id
        self.username= username
        self.password= password