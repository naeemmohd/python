# First of all we import class/module Flask and then jsonify method -  from flask import Flask, jsonify
# Then we create a flask application with __name__ to give a dynamic name to the application - flaskApp = Flask(__name__)
# Then we start writing decorators and their methods for '/'(home/root) GET request and '/products' GET request
# For the root resource here are the details - Resource: / Method : GET - e.g http://127.0.0.1:5000/
# For the products resource here are the details - Resource: /products Method : GET - e.g http://127.0.0.1:5000/products
# Finally we run the server application on a specific port. The server is ready and listening for any requests
# create a file app_v1.py using command in termimal window - nano app_v1.py
# from package flask, import class/module Flask and jsonify
from flask import Flask, jsonify
flaskApp = Flask(__name__)

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
# the root resource - Resource: / Method : GET - e.g http://127.0.0.1:5000/
@flaskApp.route('/')
def GetHome():
    return "Welcome to Products REST API Flask Home page"

# the products resource - Resource: /products Method : GET - e.g http://127.0.0.1:5000/products
@flaskApp.route('/products')
def GetAllProducts():
    return jsonify("products", products)

# run the app on a specific port
flaskApp.run(port=5000)

# Execute this file in the terminal window using command - python app_v1.py
# and watch the output for the website endpoint
