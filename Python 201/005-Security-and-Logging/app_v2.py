from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt  import JWT, jwt_required, current_identity
from securityfunctions_v2 import checkIdentity, checkAuthenticity
from datetime import timedelta

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

# to return custom resposne in addition to just tje token( here user id also)
@jwt.auth_response_handler
def custom_response_handler(access_token, identity):
    return jsonify({
                        'access_token': access_token.decode('utf-8'),
                        'user_id': identity.id
                   })


products = []

class Product(Resource):
    # add a parser
    parser = reqparse.RequestParser()
    # add argument to the parser by defining the type, if required and any help messages
    parser.add_argument('price', type=float, required=True, help= "Price can not be blank." )

    @jwt_required() # means JWT is required for this method
    def get(self, name):
        product = next(filter(lambda x: x['name'] == name, products), None)
        return {'product': product}, 200 if product else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, products), None):
            return {'maessage' : 'Item with {} name already exists.'.format(name)}, 400 # 400 for bad request

        # request.get_json() is replaced by Product.parser.parse_args()
        # data = request.get_json()
        data = Product.parser.parse_args()
        product = {'name' : name, 'price' : data['price']}
        products.append(product)
        return product, 201 

    @jwt_required() 
    def delete(self, name):
        global products
        products = list(filter(lambda x: x['name'] != name, products))
        return {'message': 'Item {} deleted'.format(name)}, 203
    
    @jwt_required()
    def put(self, name):
        data = Product.parser.parse_args()
        product = next(filter(lambda x: x['name']==name, products), None)
        if product:
            product.update(data)
            return product, 200
        else:
            product = {'name' : name, 'price' : data['price']}
            products.append(product)
            return product, 201 

# add resource to Api
restApi.add_resource(Product,'/product/<string:name>')

# for getting list of products
class Products(Resource):
    #define get method
    def get(self):
        return products
# add resource to Api
restApi.add_resource(Products,'/products')

flaskApp.run(port=5000, debug=True)
