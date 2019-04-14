from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt  import JWT, current_identity
from datetime import timedelta

from securityutils import checkIdentity, checkAuthenticity
from resources.userresources import UserSignOn
from resources.productresources import Product, Products
from resources.categoryresources import Category, Categories

flaskApp = Flask(__name__)
flaskApp.config['PROPAGATE_EXCEPTIONS'] = True # to enforce propagate an exception even if debug is set to false
flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'  # to enforce /login as the auth page rather then /auth
flaskApp.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # to enforce JSON web token expiration to a custom value in seconds. Defaults to 300 seconds(5 minutes)
flaskApp.config['JWT_AUTH_USERNAME_KEY'] = 'email' # to enforce AUTH key as email rather than default username
flaskApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbdata.db' # path of the databse - root of project
flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # enforce using SQLAlchemy session tracking rather than Flask-SQLAlchemy
flaskApp.secret_key = "%!!#@#^*&^%$^#%@"
restApi = Api(flaskApp)
jwt = JWT(flaskApp, checkAuthenticity, checkIdentity)

@flaskApp.before_first_request
def setupDatabase():
    db.create_all()

# to return custom resposne in addition to just the token(here user id also)
@jwt.auth_response_handler
def custom_response_handler(access_token, identity):
    return jsonify({ 'access_token': access_token.decode('utf-8'), 'user_id': identity.id })

# add resource to Api
restApi.add_resource(Product,'/product/<string:name>')
restApi.add_resource(Products,'/products')
restApi.add_resource(Category,'/category/<string:name>')
restApi.add_resource(Categories,'/categories')
restApi.add_resource(UserSignOn,'/register')

if __name__ == '__main__':
    # in the main app import the db SQLAlchemy object and initialize it using init_app(flaskApp)
    from dbutils import db
    db.init_app(flaskApp)
    flaskApp.run(port=5000, debug=True)
