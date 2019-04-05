#create a User model class to represent a user and its credentials
class User(object):
    def __init__(self, _id, email, password):
        self.id= _id
        self.email= email
        self.password= password