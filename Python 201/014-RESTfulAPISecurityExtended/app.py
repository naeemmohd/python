import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended  import JWTManager
from datetime import timedelta

from securityutils import checkIdentity, checkAuthenticity
from resources.userresources import User, UserSignOn, UserSignIn, UserTokenRefresh, UserLogout
from resources.productresources import Product, Products
from resources.categoryresources import Category, Categories
from models.usermodel import UserModel
from blacklistdata import BLACKLISTED_JTIs, BLACKLISTED_USERS

flaskApp = Flask(__name__)
flaskApp.config['PROPAGATE_EXCEPTIONS'] = True # to enforce propagate an exception even if debug is set to false
flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'  # to enforce /login as the auth page rather then /auth
flaskApp.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=120) # to enforce JSON web token expiration to a custom value in seconds. Defaults to 300 seconds(5 minutes)
flaskApp.config['JWT_AUTH_USERNAME_KEY'] = 'email' # to enforce AUTH key as email rather than default username

# path of the databse - root of project - DATABASE_URL is a os level variable in Heroku after you have connected to Postgres
flaskApp.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///dbdata.db')

flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # enforce using SQLAlchemy session tracking rather than Flask-SQLAlchemy
flaskApp.config['JWT_SECRET_KEY'] = '@#!~%^&*()_#$%^%' # secret jey for JWT seperately 
flaskApp.secret_key = "%!!#@#^*&^%$^#%@" # secret key of the flask app

# blacklisting users, IPs etc
flaskApp.config['JWT_BLACKLIST_ENABLED'] = True # enables blacklisting
flaskApp.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh'] # enables blacklisting for access as well as refresh tokens


restApi = Api(flaskApp)

# The JWT manager - does not create a auth end points, just lives under the app
# jwt = JWT(flaskApp, checkAuthenticity, checkIdentity)
jwt = JWTManager(flaskApp)

# called when no a blacklisted user logs in, it returns TRUE id blacklisted and automatically calls token revoke
@jwt.token_in_blacklist_loader
def blacklistedUsersCallback(decrypted_token):
    if decrypted_token['jti']:
        return decrypted_token['jti'] in BLACKLISTED_JTIs
    return decrypted_token['identity'] in BLACKLISTED_USERS

# is executed to generated a custom claim
@jwt.user_claims_loader
def addClaimsToJWT(identity):
    user = UserModel.getUserById(identity)
    if user.isadmin == 1:
        return {'isadmin' : True}
    return {'isadmin' : False}

# is executed then application's token is expired and what action to do after token expiration
# This function replaces the out of box token expiration message
@jwt.expired_token_loader
def expiredTokenCallback():
    return jsonify({
        'errorcode' : 'TokenExpired',
        'errormessage' : 'The access token has expired, Please refresh or login.'
    }), 401

@jwt.invalid_token_loader
def invalidTokenCallback(error):
    return jsonify({
       'errorcode' : 'TokenInvalid',
       'errormessage' : 'The token is invalid, please check JWT Authorization header.' 
    }), 401

# called when no JWT is send in Authorization header
@jwt.unauthorized_loader
def unauthorizedTokenCallback(error):
    return jsonify({
       'errorcode' : 'TokenUnAuthorized',
       'errormessage' : 'The token is unauthorized please pass JWT token in Authorization header.' 
    }), 401

# called whena token is revoked
@jwt.revoked_token_loader
def revokedTokenCallback():
    return jsonify({
       'errorcode' : 'TokenRevoked',
       'errormessage' : 'The token is revoked, please check with web master if you are a black listed user or your token is expired, please relogin.' 
    }), 401

# called whena fresh token is needed but a non-fresh token is passed
@jwt.needs_fresh_token_loader
def needsFreshTokenCallback():
    return jsonify({
       'errorcode' : 'FreshTokenNeeded',
       'errormessage' : 'A fresh token is needed, please refresh the token by logging in(not by refreshing).' 
    }), 401
    
@flaskApp.before_first_request
def setupDatabase():
    db.create_all()

# add resource to Api
restApi.add_resource(Product,'/product/<string:name>')
restApi.add_resource(Products,'/products')
restApi.add_resource(Category,'/category/<string:name>')
restApi.add_resource(Categories,'/categories')
restApi.add_resource(UserSignOn,'/register')
restApi.add_resource(User,'/user/<int:userid>')
restApi.add_resource(UserSignIn,'/login')
restApi.add_resource(UserTokenRefresh,'/tokenrefresh')
restApi.add_resource(UserLogout,'/logout')

if __name__ == '__main__':
    # in the main app import the db SQLAlchemy object and initialize it using init_app(flaskApp)
    from dbutils import db
    db.init_app(flaskApp)
    flaskApp.run(port=5000, debug=True)
