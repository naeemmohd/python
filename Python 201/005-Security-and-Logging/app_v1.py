from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt  import JWT, jwt_required, current_identity
from securityfunctions import checkIdentity, checkAuthenticity

flaskApp = Flask(__name__)

# add a secret key 
flaskApp.config['PROPAGATE_EXCEPTIONS'] = True # to force propagate an exception even if debug is set to false
flaskApp.secret_key = "%!!#@#^*&^%$^#%@"
restApi = Api(flaskApp)

# create a JWT 
jwt = JWT(flaskApp, checkAuthenticity, checkIdentity)

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
