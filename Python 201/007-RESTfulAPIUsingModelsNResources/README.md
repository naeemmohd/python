### Using models and resources in RESTful APIs:
  * What is ***Seperation of concerns***?
    * Although our last exercise (006-RESTfulAPIWithDatabases) worked nicely but there can some issues
      * all files were put under a root folder
      * The UserDAL.py file contained classes like 'User' which is not a resource with the class 'UseSignOn' which is a resource
      * The ProductDAL.py file contained two classes Product and Products(for list of Products) but there were methods in the classes with were not resource methods
    * Maintaining such a project if it grows in size will become a nightmare if files are not put into proper folders(called packages in python).
    * Package is just like a folder which contains a python files with a special file named as '__init__.py'
    * This commands the Python interpretor to look for specific python files in respective folders and treat those folders as packages. So you can use a term like 'from models.User import user'
    * 'models' and 'resources' packages can thus be created to store classes with are models and classes which are resources.
    * Thus we are seperating the concerns and classes in 'models' package will have the responsibility of being a model only and those in 'resources' class of being a resource only.

### Setting up the ***UserModel*** model class in 'models' package:
  * Create a folder named 'models' in the root folder(E.g. 007-RESTfulAPIUsingModelsNResources here)
  * Also create a file named '__init__.py' in the 'models' folder - this file will command the Python interpretor to look for specific files in the folder and treat the folder as a package
  * Now create the ***UserModel*** model class as below:
    * Features of the UserModel model class:
      * it only imports required modules not anything related to Flask, Flask-JWT, flask_restful etc
      * adds an '__init__' method to initialize the model
      * holds two class methods - 'getUserById' and 'getUserByEmail' which connects to database and return data
      * There is no other functionality incorporated in the model
    ```
    import sqlite3

    class UserModel:
        dbName= "dbProducts.db"
        tblName= 'tblUsers'

        def __init__(self, _id, email, username, password):
            self.id= _id
            self.email= email
            self.username= username
            self.password= password
            
        @classmethod
        def getUserById(cls, _id):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()
            selectQuery = "SELECT * FROM {tableName} WHERE id=?".format(tableName=cls.tblName)
            retValue = dbCursor.execute(selectQuery, (_id,))
            oneRow = retValue.fetchone()
            if oneRow:
                user = cls(*oneRow)
            else:
                user = None
            dbConnection.close()
            return user

        @classmethod
        def getUserByEmail(cls, email):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()
            selectQuery = "SELECT * FROM {tableName} WHERE email=?".format(tableName=cls.tblName)
            retValue = dbCursor.execute(selectQuery, (email,))
            oneRow = retValue.fetchone()
            if oneRow:
                user = cls(*oneRow)
            else:
                user = None
            dbConnection.close()
            return user
    ```

### Setting up the ***ProductModel*** model class 'models' package:
  * Now create the ***ProductModel*** class as below:
    * Features of the ProductModel model class:
      * it only imports required modules not anything related to Flask, Flask-JWT, flask_restful etc
      * adds an '__init__' method to initialize the model
      * adds a 'json(self)' mothod to return the json representation of the ProductModel class object
      * holds three methods - 'getProductByName', 'AddProduct'  and 'UpdateProduct'
      * We are using 'self' keyword to refer to class elements e.g. self.dbName, self.tblName, self.name, self.desc, self.price, self.qty etc where ever needed
      * There is no other functionality incorporated in the model
    ```
    import sqlite3

    class ProductModel:
        dbName= "dbProducts.db"
        tblName= 'tblProducts'

        def __init__(self, name, desc, price, qty):
            self.name= name
            self.desc= desc
            self.price= price
            self.qty= qty
        
        def json(self):
            return {'name' : self.name, 'desc' : self.desc, 'price' : self.price, 'qty' : self.qty}

        @classmethod
        def getProductByName(cls, name):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()
            selectQuery = "SELECT * FROM {tableName} WHERE name=?".format(tableName=cls.tblName)
            retValue = dbCursor.execute(selectQuery, (name,))
            oneRow = retValue.fetchone()
            dbConnection.close()

            if oneRow:
                return cls(*oneRow)

        def AddProduct(self):
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()

            insertQuery = "INSERT INTO {tableName} VALUES(?,?,?,?)".format(tableName=self.tblName)
            
            dbCursor.execute(insertQuery, (self.name, self.desc, self.price, self.qty))

            dbConnection.commit()
            dbConnection.close()

        def UpdateProduct(self):
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()

            updateQuery = "UPDATE {tableName} SET desc=?, price=?, qty=? WHERE name=?".format(tableName=self.tblName)
            
            dbCursor.execute(updateQuery, (self.desc, self.price, self.qty, self.name))

            dbConnection.commit()
            dbConnection.close()
    ```
### Setting up the ***UserSignOn*** resource class in 'resources' package:
  * Create a folder named 'resources' in the root folder(E.g. 007-RESTfulAPIUsingModelsNResources here)
  * Also create a file named '__init__.py' in the 'resources' folder - this file will command the Python interpretor to look for specific files in the folder and treat the folder as a package
  * Now create the ***UserSignOn*** resource class as below:
    * Features of the UserSignOn resource class:
      * Since it has to use the 'UserModel' class it refrences it by using - 
        * ***from models.user import UserModel***
      * ***UserModel.getUserByEmail(emailId)*** call executes the 'getUserByEmail' method from 'UserModel' model class in 'post' method of 'UserSignOn' resource class
      * There is no other functionality incorporated in the resource class
    ```
    import sqlite3
    from flask_restful import Resource, reqparse
    from models.user import UserModel

    class UserSignOn(Resource):
        dbName= "dbProducts.db"
        tblName= 'tblUsers'

        # define parser
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, required=True, help="Email can not be blank.")
        parser.add_argument("username", type=str, required=True, help="UserName can not be blank.")
        parser.add_argument("password", type=str, required=True, help="Password can not be blank.")

        def post(self):
            data = UserSignOn.parser.parse_args()
            emailId = data['email']
            userName = data['username']
            passWord = data['password']
            
            # check if the user already exists
            if UserModel.getUserByEmail(emailId):
                returnMessage = "User with email: {email} already exists, please select a new email.".format(email=emailId)
                return {"message" : returnMessage }, 400
            
            # otherwise sign on the new user
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()

            insertQuery = "INSERT INTO {tableName} VALUES(NULL,?,?,?)".format(tableName=self.tblName)

            retValue = dbCursor.execute(insertQuery, (emailId, userName, passWord))

            dbConnection.commit()
            dbConnection.close()

            returnMessage = "Congrats {usernm} !!!, Your have been successful registerted with email: {email}.".format(usernm=userName, email=emailId)
            return {"message" : returnMessage }, 201
    ```

### Setting up the ***Product and Products*** resource classes in 'resources' package:
  * Now create the ***Product*** resource class as below:
    * Features of the Product resource class:
      * Since it has to use the 'ProductModel' class it refrences it by using - 
        * ***from models.product import ProductModel***
      * ***ProductModel.getProductByName(name)*** call executes the 'getProductByName' method from 'ProductModel' model class in 'get' method of 'Product' resource class
        * the method returns a ***ProductModel object*** therefore ***product.json()*** method is called to return JSON object to the caller(clients)
      * Similarly in the 'post' method you can initialize a ProductModel object by using - ***new_product = ProductModel(name, desc, price, qty)*** and also call ***new_product.AddProduct()*** method to add an product
      * Similarly in the 'put' method you can initialize a ProductModel object by using - ***updated_product = ProductModel(name, desc, price, qty)*** and also call ***updated_product.UpdateProduct()*** and ***updated_product.UpdateProduct()*** method to add and update a product respectively
      * The 'delete' mothod does not reference the ProductModel model class
      * The 'get' method of 'Products' class is also unchanged as it also does not reference the ProductModel model class
      * There is no other functionality incorporated in the resource class
    ```
    import sqlite3
    from flask_restful import Resource, reqparse
    from flask_jwt import jwt_required
    from models.product import ProductModel

    #create a Product model class to represent a Product and its operations
    class Product(Resource):
        dbName= "dbProducts.db"
        tblName= 'tblProducts'

        # define parser
        parser = reqparse.RequestParser()
        parser.add_argument("desc", type=str, required=True, help="Product Description can not be blank.")
        parser.add_argument("price", type=float, required=True, help="Product Price can not be blank.")
        parser.add_argument("qty", type=float, required=True, help="Product Quantity can not be blank.")

        @jwt_required()
        def get(self, name):
            product = ProductModel.getProductByName(name)
            if product:
                return product.json()
            else:
                return {"message" : "Product by the name {pname} not found!!!".format(pname=name)}, 404

        @jwt_required()
        def post(self, name):
            # check if the product exists
            if ProductModel.getProductByName(name):
                return {"message" : "Product by the name {pname} already exists, select a new name!!!".format(pname=name)}, 400

            # otherwise insert the new product
            data = Product.parser.parse_args()
            desc = data['desc']
            price = data['price']
            qty = data['qty']

            new_product = ProductModel(name, desc, price, qty)
            try:
                new_product.AddProduct()
                returnMessage = "Congrats, Product by the name : {pname} has been ADDED.".format(pname=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 500 
            # return new_product

        @jwt_required()
        def put(self, name):
            product = ProductModel.getProductByName(name)

            data = Product.parser.parse_args()
            desc = data['desc']
            price = data['price']
            qty = data['qty']

            updated_product = ProductModel(name, desc, price, qty)

            if product:
                try:
                    updated_product.UpdateProduct()
                    returnMessage = "Congrats, Product by the name : {pname} has been UPDATED.".format(pname=name)
                    return {"message" : returnMessage }
                except:
                    return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully UPDATED!!!".format(pname=name)}, 500 
            else:
                try:
                    updated_product.AddProduct()
                    returnMessage = "Congrats, Product by the name : {pname} has been ADDED.".format(pname=name)
                    return {"message" : returnMessage }
                except:
                    return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 500 
            # return updated_product
            
        @jwt_required()
        def delete(self, name):
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()
            deleteQuery = "DELETE FROM {tableName} WHERE name=?".format(tableName=self.tblName)
            dbCursor.execute(deleteQuery, (name,))
            
            dbConnection.commit()
            dbConnection.close()
            return {"message" : "Product by the name {pname} DELETED!!!".format(pname=name)}



    #create a Products model class to represent list of Products and its operations
    class Products(Resource):
        dbName= "dbProducts.db"
        tblName= 'tblProducts'
        
        @jwt_required()
        def get(self):
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()
            selectQuery = "SELECT * FROM {tableName}".format(tableName=self.tblName)
            retValue = dbCursor.execute(selectQuery)

            products=[]
            for product in retValue:
                products.append({'name': product[0], 'desc': product[1], 'price': product[2], 'qty': product[3]})
            
            dbConnection.close()

            return {"products" : products}, 200
    
    ```
 
 ### Updates in the ***securityutils*** script:
  * Only minor updates regarding the import statement and referencing the UserModel class:
    * Refrencing the UserModel class - ***from models.user import UserModel***
    * ***UserModel.getUserByEmail(email)*** is called to check user by email and ***UserModel.getUserById(userId)*** to check user by id
    * There is no other functionality change
    ```
    # import custom module to use the User model to create users
    from models.user import UserModel

    # import safe_str_cmp to safe compare ascii or unicode based strings
    from werkzeug.security import safe_str_cmp

    # check identity based on payload
    def checkIdentity(payload):
        userid= payload['identity']
        return UserModel.getUserById(userid)

    # check/authenticate user 
    def checkAuthenticity(email, password):
        user = UserModel.getUserByEmail(email)
        if user and safe_str_cmp(user.password, password):
            return user

    ```

### Updates in the ***app_v1.py*** script:
  * Only minor updates regarding the import statement and referencing the UserSignOn, Product and Products resource classes:
    * Refrencing the resource class - 
      * ***from resources.users import UserSignOn*** and
      * ***from resources.products import Product, Products***
    * The resources classes are called in the 3 lines as below:
      * restApi.add_resource(Product,'/product/<string:name>')
      * restApi.add_resource(Products,'/products')
      * restApi.add_resource(UserSignOn,'/register')
    * There is no other functionality change
    ```
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

    ```
 ### Testing the project:
  - Now the project is ready for testing, you can repeat all the operations you tested in previous exercise like register, login, add a product, update a product, delete a product, get one product, get all products. 
  - Since we did not change the functionality and just refactored and categorized the project into packages everything should run perfectly as before