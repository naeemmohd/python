import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

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
        userName = data['username']
        passWord = data['password']
        
        # check if the user already exists
        if UserModel.getUserByEmail(emailId):
            returnMessage = "User with email: {email} already exists, please select a new email.".format(email=emailId)
            return {"message" : returnMessage }, 400
        
        # otherwise sign on the new user
        dbConnection = sqlite3.connect(self.dbName)
        dbCursor = dbConnection.cursor()

        insertQuery = "INSERT INTO {tableName} VALUES(NULL,?,?,?)".format(tableName=self.tblName)

        retValue = dbCursor.execute(insertQuery, (emailId, userName, passWord))

        dbConnection.commit()
        dbConnection.close()

        returnMessage = "Congrats {usernm} !!!, Your have been successful registerted with email: {email}.".format(usernm=userName, email=emailId)
        return {"message" : returnMessage }, 201