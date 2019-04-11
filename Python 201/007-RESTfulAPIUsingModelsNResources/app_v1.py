from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt  import JWT, current_identity
from datetime import timedelta

from securityutils import checkIdentity, checkAuthenticity
from resources.users import UserSignOn
from resources.products import Product, Products

flaskApp = Flask(__name__)

# add a secret key 
flaskApp.config['PROPAGATE_EXCEPTIONS'] = True # to enforce propagate an exception even if debug is set to false
flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'  # to enforce /login as the auth page rather then /auth
flaskApp.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # to enforce JSON web token expiration to a custom value in seconds. Defaults to 300 seconds(5 minutes)
flaskApp.config['JWT_AUTH_USERNAME_KEY'] = 'email' # to enforce AUTH key as email rather than default username
flaskApp.secret_key = "%!!#@#^*&^%$^#%@"

restApi = Api(flaskApp)

# create a JWT 
jwt = JWT(flaskApp, checkAuthenticity, checkIdentity)

# to return custom resposne in addition to just the token(here user id also)
@jwt.auth_response_handler
def custom_response_handler(access_token, identity):
    return jsonify({
                        'access_token': access_token.decode('utf-8'),
                        'user_id': identity.id
                   })

# add resource to Api
restApi.add_resource(Product,'/product/<string:name>')
restApi.add_resource(Products,'/products')
restApi.add_resource(UserSignOn,'/register')

if __name__ == '__main__':
    flaskApp.run(port=5000, debug=True)
