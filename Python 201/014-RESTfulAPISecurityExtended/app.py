import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended  import JWTManager
from datetime import timedelta

from securityutils import checkIdentity, checkAuthenticity
from resources.userresources import User, UserSignOn, UserSignIn
from resources.productresources import Product, Products
from resources.categoryresources import Category, Categories
from models.usermodel import UserModel

flaskApp = Flask(__name__)
flaskApp.config['PROPAGATE_EXCEPTIONS'] = True # to enforce propagate an exception even if debug is set to false
flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'  # to enforce /login as the auth page rather then /auth
flaskApp.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=300) # to enforce JSON web token expiration to a custom value in seconds. Defaults to 300 seconds(5 minutes)
flaskApp.config['JWT_AUTH_USERNAME_KEY'] = 'email' # to enforce AUTH key as email rather than default username

# path of the databse - root of project - DATABASE_URL is a os level variable in Heroku after you have connected to Postgres
flaskApp.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///dbdata.db')

flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # enforce using SQLAlchemy session tracking rather than Flask-SQLAlchemy
flaskApp.config['JWT_SECRET_KEY'] = '@#!~%^&*()_#$%^%' # secret jey for JWT seperately 
flaskApp.secret_key = "%!!#@#^*&^%$^#%@" # secret key of the flask app
restApi = Api(flaskApp)

# The JWT manager - does not create a auth end points, just lives under the app
# jwt = JWT(flaskApp, checkAuthenticity, checkIdentity)
jwt = JWTManager(flaskApp)

@jwt.user_claims_loader
def addClaimsToJWT(identity):
    user = UserModel.getUserById(identity)
    if user.isadmin == 1:
        return {'isadmin' : True}
    return {'isadmin' : False}

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

if __name__ == '__main__':
    # in the main app import the db SQLAlchemy object and initialize it using init_app(flaskApp)
    from dbutils import db
    db.init_app(flaskApp)
    flaskApp.run(port=5000, debug=True)
