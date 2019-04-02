#import Flask class from flask package
from flask import Flask, request
#import Flask class from flask_restful package - 
# Api represents an API and a Resource represents a resource which will support methods(HTTP verbs)
from flask_restful import Resource, Api

# create a flask app
flaskApp = Flask(__name__)

#create an API 
restApi = Api(flaskApp)

# currently using in memory list
products = []

#create a class product which will represent a resource(will extend from Resource type class)
class Product(Resource):
    #define get method
    def get(self, name):
        for product in products:
            if product['name'] == name:
                return product
        # See this statement : ***return {'product': None}, 404***
        # We are not only retuning a valid JSON but also a 404 status code when a product is not found
        return {'product': None}, 404
    #define post method
    def post(self, name):
        # See this statement : ***data = request.get_json()***  
        # See how we are using the request object to retrive data from request body
        data = request.get_json()
        product = {'name' : name, 'price' : data['price']}
        products.append(product)
        # See this statement : ***return product, 201***  
        # We are not only retuning a valid JSON but also a 201 status code when a product is created
        return product, 201

# add resource to Api
restApi.add_resource(Product,'/product/<string:name>')

# for getting list of items
class Products(Resource):
    #define get method
    def get(self):
        return products

# add resource to Api
restApi.add_resource(Products,'/products')

# run the app on a specific port
# See this statement : ***flaskApp.run(port=5000, debug=True***  
# If something goes wrong, flask will return a nice error message if debug=True
flaskApp.run(port=5000, debug=True)
