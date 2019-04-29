# import the db SQLAlchemy object
from dbutils import db

# UserModel class will extend/inherit from db.Model class
class UserModel(db.Model):

    # define the table name for OR mapping
    __tablename__= 'tblUsers'

    # define the table schema for the OR mapping
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    isadmin = db.Column(db.Integer)
    
    def __init__(self, email, username, password, isadmin):
        self.email= email
        self.username= username
        self.password= password
        self.isadmin= isadmin

    def json(self):
        return { 
            "id" : self.id, 
            "email" : self.email, 
            "username" : self.username,
            "isadmin" : self.isadmin
            #,"password" : self.password 
        }


    @classmethod
    def getUserById(cls, _id):
        # cls.query returns all rows like Select * from tblUsers
        # cls.query.filter_by(id=_id) retuns the filtered rows like Select * from tblUsers where id = _id
        # cls.query.filter_by(id=_id).first() returns the top 1 row like Select * from tblUsers where id = _id LIMIT 1
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def getUserByEmail(cls, email):
        return cls.query.filter_by(email=email).first()

    def Save(self):
        db.session.add(self)
        db.session.commit()
    
    def Delete(self):
        db.session.delete(self)
        db.session.commit()