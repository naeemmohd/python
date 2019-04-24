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

    def __init__(self, email, username, password):
        self.email= email
        self.username= username
        self.password= password

    def json(self):
        return { "email" : self.email, "username" : self.username, "password" : self.password }


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