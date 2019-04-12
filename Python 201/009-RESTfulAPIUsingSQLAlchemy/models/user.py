from SQLAlchemyDB import sqlAlchemyDb

class UserModel(sqlAlchemyDb.Model):

    __tablename__= 'tblUsers'

    id = sqlAlchemyDb.Column(sqlAlchemyDb.Integer, primary_key=True)
    email = sqlAlchemyDb.Column(sqlAlchemyDb.String(100))
    username = sqlAlchemyDb.Column(sqlAlchemyDb.String(100))
    password = sqlAlchemyDb.Column(sqlAlchemyDb.String(100))

    def __init__(self, email, username, password):
        self.email= email
        self.username= username
        self.password= password
        
    @classmethod
    def getUserById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def getUserByEmail(cls, email):
        return cls.query.filter_by(email=email).first()

    def Save(self):
        sqlAlchemyDb.session.add(self)
        sqlAlchemyDb.session.commit()
    
    def Delete(self):
        sqlAlchemyDb.session.delete(self)
        sqlAlchemyDb.session.commit()