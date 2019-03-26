# First of all we import class/module Flask and then jsonify method -  from flask import Flask, jsonify
# Then we create a flask application with __name__ to give a dynamic name to the application - flaskApp = Flask(__name__)
# Then we start writing decorators and their methods for '/'(home/root) GET request and '/products' GET request
# For the root resource here are the details - Resource: / Method : GET - e.g http://127.0.0.1:5000/
# For the products resource here are the details - Resource: /products Method : GET - e.g http://127.0.0.1:5000/products
# For the category resource here are the details for GET - Resource: /category/<string:category> Method : GET - e.g http://127.0.0.1:5000/category/desktops
# For the category resource here are the details for POST - Resource: /category Method : POST - e.g http://127.0.0.1:5000/category
# For the product resource are the details for GET - Resource: /category/<string:category>/product Method : GET - e.g http://127.0.0.1:5000/category/desktops/product
# For the product resource are the details for POST - Resource: /category/product Method : POST - e.g http://127.0.0.1:5000/category/desktops
# Finally we run the server application on a specific port. The server is ready and listening for any requests
# from package flask, import class/module Flask, jsonify method and request method
from flask import Flask, jsonify, request
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
def GetProducts():
  return jsonify("products", products)

# the category resource - Resource: /category Method : GET - e.g http://127.0.0.1:5000/category/desktops
@flaskApp.route('/category/<string:category>')
def GetCategory(category):
  for categ in products:
    if categ['category'] == category:
      return jsonify(categ)
  return jsonify({"message" : "category does not exist"})

# the category resource - Resource: /category Method : POST - e.g http://127.0.0.1:5000/category
@flaskApp.route('/category', methods=['POST'])
def CreateCategory():
    data = request.get_json()
    new_category = {
      "category" : data["category"],
      "items" : []
    }
    products.append(new_category)
    return jsonify(new_category)

# the product resource - Resource: /category/product Method : GET - e.g http://127.0.0.1:5000/category/desktops/product
@flaskApp.route('/category/<string:category>/product')
def GetProductFromCategory(category):
  for categ in products:
    if categ['category'] == category:
        return jsonify( {'items':categ['items'] } )
  return jsonify ({'message':'category/product not found'})
  
# the product resource - Resource: /category/product Method : POST - e.g http://127.0.0.1:5000/category/desktops
@flaskApp.route('/category/<string:category>' , methods=['POST'])
def CreateProductInCategory(category):
  data = request.get_json()
  for categ in products:
    if categ['category'] == category:
      new_item = {
          'name': data['name'],
          'price': data['price']
      }
      categ['items'].append(new_item)
      return jsonify(new_item)
  return jsonify ({'message' :'category/product not found'})

# run the app on a specific port
flaskApp.run(port=5000)
