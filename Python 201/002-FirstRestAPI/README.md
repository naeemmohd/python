### How do servers work:
  * Servers - are applications which return information when request by a HTTP client application.
  * Browsers - Browsers are HTTP client applications which send request to servers to retrieve information
  * Request - a browser sends a Request with requested information to server
  * Response - a server responds to a request via a response
  * Types of response - HTML, JSON, Text, Error, Nothing

### HTTP verbs:
  * are commands through which a request is sent to server and response is retrieved
  * HTTP verb | Action | Example 
    ------------ | ------------- | -------------
    GET | Read | E.g. http://127.0.0.1:5000/products - retieves list of products
    PUT | Update/Replace | E.g. http://127.0.0.1:5000/product/1 - updates/replaces product 1
    POST | Create | E.g. http://127.0.0.1:5000/product/1 - creates product 1
    DELETE | Delete | E.g. http://127.0.0.1:5000/product/1 - deletes product 1, 
    PATCH | Update/Modify | E.g. http://127.0.0.1:5000/products - updates/modifies product 1, 

### JSON:
  * it is a kind of dictionary(key-pair values) but it is a string
  * open-standard for communication between clients and servers
  * E.g of a products JSON string - 
    [
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

### REST API:
  * an architecture/mechanism of defining and API exploting the power of HTTP verbs using HTTP protocol
  * Stateless - 
    * Each request/response (E.g GET, PUT etc)  is completely unaware of state of the other 
    * GET is not aware what PUT is doing 
  * Resource - and API is made up of resources and methods
    * E.g. In http://127.0.0.1:5000/product/1, http://127.0.0.1:5000/products
    * Product and Products are two resources 
    * When a clinet/brower requests a resource, the server response by executing a method(E.g GET, PUT)
  * Method - are the HTTP verbs which are executed to return the response to the client
    * E.g In http://127.0.0.1:5000/product/1 - GET will return product 1
    * E.g In http://127.0.0.1:5000/products - GET will return all products

### First REST API Setup:
  * We will extend our previous app.py server application to add routes for the above verbs.
    ```
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

    
    ```
  * Please see screen shot below
    * The app_v1.py codeL
    ![Python versions](../images/002-02-FirstRestAPI-ServerCode.png)
    * The browser output:
    ![Python versions](../images/002-02-FirstRestAPI-BrowserOutput.png)