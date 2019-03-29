# import Flask class from flask package
from flask import Flask, request, jsonify
# import Flask class from flask_restful package - 
# Api represents an API and a Resource represents a resource which will support methods(HTTP verbs)
from flask_restful import Resource, Api

# create a flask app
flaskApp = Flask(__name__)

#create an API 
restApi = Api(flaskApp)

# create a class Student which will represent a resource(will extend from Resource type class)
class Home(Resource):
    # define get method for home
    def get(self):
        return "Welcome to Products RESTful API Flask Home page"
# add resource to Api. e.g. http://127.0.0.1:5555/ 
restApi.add_resource(Home,'/' )

# create a class Student which will represent a resource(will extend from Resource type class)
class Products(Resource):
    # define get method for home
    def get(self):
        return jsonify("products", products)
# add resource to Api. e.g. http://127.0.0.1:5555/products
restApi.add_resource(Products,'/products' )

# currently storing products in this dictionary(in actual scenario, you may save it to database)
products = [
      {
        "category" : "laptops",
        "items" : [
          {
            "name" : "HP 360",
            "price" : 599.99
          },
          {
            "name" : "HP Pavilion",
            "price" : 699.99
          }
        ]
      }
    ]

# run the app on a specific port
flaskApp.run(port=5555)
