from flask_restful import Resource, reqparse
# flask_jwt_extended is imported for the two methods create_access_token and create_refresh_token
from flask_jwt_extended import create_access_token, create_refresh_token
from models.usermodel import UserModel
from werkzeug.security import safe_str_cmp

# define parser
_parser = reqparse.RequestParser()
_parser.add_argument("email", type=str, required=True, help="Email can not be blank.")
_parser.add_argument("username", type=str, required=True, help="UserName can not be blank.")
_parser.add_argument("password", type=str, required=True, help="Password can not be blank.")
_parser.add_argument("isadmin", type=int, required=True, help="Is Admin can not be blank.")

class UserSignOn(Resource):

    def post(self):
        data = _parser.parse_args()
        emailId = data['email']
                
        # check if the user already exists
        if UserModel.getUserByEmail(emailId):
            returnMessage = "User with email: {email} already exists, please select a new email.".format(email=emailId)
            return {"message" : returnMessage }, 400
        
        # otherwise sign on the new user
        user = UserModel(**data)
        user.Save()

        returnMessage = "Congrats {usernm} !!!, Your have been successful registerted with email: {email}.".format(usernm=data['username'], email=emailId)
        return {"message" : returnMessage }, 201

class User(Resource):

    @classmethod
    def get(cls, userid):
        user = UserModel.getUserById(userid)
        if user:
            return user.json(), 200
        return {"message" : "User by the Id {userid} not found!!!".format(userid=userid)}, 404
    
    @classmethod
    def delete(cls, userid):
        user = UserModel.getUserById(userid)
        if user:
            user.Delete()
            return {"message" : "User by the Id {userid} DELETED!!!".format(userid=userid)}, 200
        return {"message" : "User by the Id {userid} not found!!!".format(userid=userid)}, 404

class UserSignIn(Resource):

    @classmethod
    def post(cls):
        # first get the data from the parser 
        data = _parser.parse_args()
        emailId = data['email']
        passwd = data['password']
                
        # check if the user exists in database
        user = UserModel.getUserByEmail(emailId)

        # check and verify the password
        if user and safe_str_cmp(user.password, passwd):
            # create an access token
            accessToken = create_access_token(identity=user.id, fresh=True)
            refreshToken = create_refresh_token(user.id)
            return{
                'access_token' : accessToken,
                'refresh_token' : refreshToken
            }, 200

        returnInvalidCredentialsMessage = "Wrong credentials passed for user with email: {email}".format(email=emailId)
        return {
            'message' : returnInvalidCredentialsMessage
        }, 401