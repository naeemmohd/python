import sqlite3
from flask_restful import Resource, reqparse

#create a User model class to represent a user and its operations
class User(Resource):
    dbName= "dbProducts.db"
    tblName= 'tblUsers'

    def __init__(self, _id, email, username, password):
        self.id= _id
        self.email= email
        self.username= username
        self.password= password
        
    @classmethod
    def getUserById(cls, _id):
        conn = sqlite3.connect(cls.dbName)
        curs = conn.cursor()
        selectQuery = "SELECT * FROM {tableName} WHERE id=?".format(tableName=cls.tblName)
        retValue = curs.execute(selectQuery, (_id,))
        oneRow = retValue.fetchone()
        if oneRow:
            user = cls(*oneRow)
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def getUserByEmail(cls, email):
        conn = sqlite3.connect(cls.dbName)
        curs = conn.cursor()
        selectQuery = "SELECT * FROM {tableName} WHERE email=?".format(tableName=cls.tblName)
        retValue = curs.execute(selectQuery, (email,))
        oneRow = retValue.fetchone()
        if oneRow:
            user = cls(*oneRow)
        else:
            user = None
        conn.close()
        return user
    
    @classmethod
    def getUserByName(cls, name):
        conn = sqlite3.connect(cls.dbName)
        curs = conn.cursor()
        selectQuery = "SELECT * FROM {tableName} WHERE username=?".format(tableName=cls.tblName)
        retValue = curs.execute(selectQuery, (name,))
        oneRow = retValue.fetchone()
        if oneRow:
            user = cls(*oneRow)
        else:
            user = None
        conn.close()
        return user

class UserSignOn(Resource):
    dbName= "dbProducts.db"
    tblName= 'tblUsers'

    # define parser
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True, help="Email can not be blank.")
    parser.add_argument("username", type=str, required=True, help="UserName can not be blank.")
    parser.add_argument("password", type=str, required=True, help="Password can not be blank.")

    def post(self):
        data = UserSignOn.parser.parse_args()
        emailId = data['email']

        # check if the user already exists
        if User.getUserByEmail(emailId):
            returnMessage = "User with email: {email} already exists, please select a new email.".format(email=emailId)
            return {"message" : returnMessage }, 400
        
        # otherwise sign on the new user
        conn = sqlite3.connect(self.dbName)
        curs = conn.cursor()

        insertQuery = "INSERT INTO {tableName} VALUES(NULL,?,?,?)".format(tableName=self.tblName)
        userName = data['username']
        passWord = data['password']
        retValue = curs.execute(insertQuery, (emailId, userName, passWord))

        conn.commit()
        conn.close()

        returnMessage = "Congrats {usernm} !!!, Your have been successful registerted with email: {email}.".format(usernm=userName, email=emailId)
        return {"message" : returnMessage }, 201