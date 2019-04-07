### Interact with databases in RESTful APIs:
  * Flask RESTful APIs can interact with any databases
  * There are standard steps like(E.g. this exapmle is with SQLite)
    * connect to database - ***dbConnection = sqllite3.connect("mydatabase.db")***
    * creating a cursor - ***dbCursor = dbConnection.cursor()***
    * creating a SQL query - ***sqlQuery = "SELECT * FROM tblProducts"***
    * execute the SQL query - ***dbCursor.execute(sqlQuery)***
    * committing the changes(if any, if it is a INSERT, UPDATE, DELETE statement) - ***dbConnection.commit()***
    * close the connection - ***dbConnection.close()***
  * Python has many out of box modules to support connctions to various databases
    * sqlite3 - use ***import sqlite3*** - to use SQLite
    * flask.ext.mysql - use ***from flask.ext.mysql import MySQL*** - to use MySQL etc

### Setting up the database and the tables:
  * Please see the code below to setup the database and the tables
  * File name : setupdb.py - the code for setting up the database and the tables 
  * To execute this script - ***python setupdb.py***
  * The script follows the above standard steps to create a connection, set a cursor, create a SQL query, execute it. commit the changes and close the connection.
  * The statement worth highlighting is the table creation script:
    * ***sqlTblUsers = "CREATE TABLE IF NOT EXISTS tblUsers(id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT)"***
    * ***CREATE TABLE*** command is used to create the table
    * ***IF NOT EXISTS** command is used to check if the tables is already existing or not
    * ***tblUsers*** - is the table name
    * ***(id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT)*** command is used too specify the columns and data types of the columns
    * ***id, email, username, password*** as the column names
    * ***INT, TEXT, FLOAT** are the data types
    * ***INTEGER*** is specially used to make a column ***auto-incremental***, so that you dont have to insert a value for that column
    * ***PRIMARY KEY*** defines the column as the primary key which is unique and index column of the table
  * 
    ```
    # setupdb.py - code for setting up the database and the tables 
    # execute this script as - ***python setupdb.py***
    # import sqlites3 module
    import sqlite3

    # creating a connection - will create a file dbProducts.db in current location
    dbConnection = sqlite3.connect("dbProducts.db")
    # creating a cursor do work on the database
    dbCursor = dbConnection.cursor()

    # create required tables tblUsers and tblProducts
    # Data type 'INTEGER'  is used for auto-incrementing columns only othrwise you can use normal 'int'
    sqlTblUsers = "CREATE TABLE IF NOT EXISTS tblUsers(id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT)"
    sqlTblProducts = "CREATE TABLE IF NOT EXISTS tblProducts(name TEXT PRIMARY KEY, desc TEXT, price REAL, qty REAL)"

    # execute the query
    dbCursor.execute(sqlTblUsers)
    dbCursor.execute(sqlTblProducts)

    # commit changes
    dbConnection.commit()

    #close dbConnection
    dbConnection.close()
    ```
  * The app code screenshot for setting up database and tables:
    ![Setting up database and tables](../images/002-06-Settingupdatabasesandtables.png)
    ---------------------------------------------------------------------------------

### Setting up register and login features in the RESTful API:
  * Now we are going to allow users to register and login to the RESTful API
  * The registration function will be a ***POST method*** to a ***UserSignOn*** resource
    * setting up the UserSignOn resource - ***restApi.add_resource(UserSignOn,'/register')*** in file ***app_v1.py***
    * setting up the UserSignOn class with a post method in file ***userDAL.py***
    ```
    import sqlite3
    from flask_restful import Resource, reqparse

    #create a User model class to represent a user and its operations
    class User(Resource):
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
        
        @classmethod
        def getUserByName(cls, name):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()
            selectQuery = "SELECT * FROM {tableName} WHERE username=?".format(tableName=cls.tblName)
            retValue = dbCursor.execute(selectQuery, (name,))
            oneRow = retValue.fetchone()
            if oneRow:
                user = cls(*oneRow)
            else:
                user = None
            dbConnection.close()
            return user

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

            # check if the user already exists
            if User.getUserByEmail(emailId):
                returnMessage = "User with email: {email} already exists, please select a new email.".format(email=emailId)
                return {"message" : returnMessage }, 400
            
            # otherwise sign on the new user
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()

            insertQuery = "INSERT INTO {tableName} VALUES(NULL,?,?,?)".format(tableName=self.tblName)
            userName = data['username']
            passWord = data['password']
            retValue = dbCursor.execute(insertQuery, (emailId, userName, passWord))

            dbConnection.commit()
            dbConnection.close()

            returnMessage = "Congrats {usernm} !!!, Your have been successful registerted with email: {email}.".format(usernm=userName, email=emailId)
            return {"message" : returnMessage }, 201
    ```

  * The app code screenshot for UserSignOn class:
    * The UserSignOn class has a ***POST*** method to retrieve the email, username and password from client
    * It then parses the request and validates if they are not blank
    * It calls ***User.getUserByEmail(emailId)*** method to check if a user by the same email exists or not
      * if ***yes***, then returns a message that user already exists
      * if ***no***, then it retrieves the email, username and password from the parsed requuest and execute and insert SQL query to add the user to the SQLite database and returns a success message
    ![UserSignOn class](../images/002-06-UserSignOnClass.png)
    ---------------------------------------------------------------------------------

  * The app code screenshot for User class:
    * The User class actually defines two functions - getUserById and getUserByEmail
    * ***getUserById*** - method is used to get User by its Id 
      * ***selectQuery = "SELECT * FROM {tableName} WHERE id=?".format(tableName=cls.tblName)**
      * The above query retrieves the user by the id
      * It then executes the query to get results and then fetch one row from the result
        * ***retValue = dbCursor.execute(selectQuery, (_id,))***
        * ***oneRow = retValue.fetchone()***
    * ***getUserByEmail*** - method is used to get User by its Email 
      * ***selectQuery = "SELECT * FROM {tableName} WHERE email=?".format(tableName=cls.tblName)**
      * The above query retrieves the user by the email
      * It then executes the query to get results and then fetch one row from the result
        * ***retValue = dbCursor.execute(selectQuery, (email,))***
        * ***oneRow = retValue.fetchone()***
    ![UserSignOn class](../images/002-06-UserClass.png)
    ---------------------------------------------------------------------------------

  * The ***securityutils*** script:
    * The securityutils script actually defined the JWT identity(***checkIdentity***) and authenticate(***checkAuthenticity***) functions
    * ***checkIdentity*** function - 
      * is the identity function which is used to authenticate the identity of the user
      * retrives the user id from the request payload and returns the user by its id
      * it calls ***User.getUserById(userid)*** function to retrieve the user
    * ***checkAuthenticity*** function - 
      * is the authenticate function which is used to authenticate the user credentials(email an password here)
      * retrives the user by email id, validates the password returns the user if validated 
      * it calls ***User.getUserByEmail(email)*** function to retrieve the user
    ```
    # import custom module to use the User model to create users
    from userDAL import User

    # import safe_str_cmp to safe compare ascii or unicode based strings
    from werkzeug.security import safe_str_cmp

    # check identity based on payload
    def checkIdentity(payload):
        userid= payload['identity']
        return User.getUserById(userid)

    # check/authenticate user 
    def checkAuthenticity(email, password):
        user = User.getUserByEmail(email)
        if user and safe_str_cmp(user.password, password):
            return user

    ```
    * The app code screenshot for securityutils script:
    ![securityutils script](../images/002-06-securityutilsscript.png)
    ---------------------------------------------------------------------------------

  * The ***/register*** screen:
    * The following payload is passed to ***/register*** resource via ***POST** method to register
    ```
    {
      "email": "Naeemm@futurecloud.com",
      "username": "Mohd Naeem",
      "password": "PassNaeem"
    }
    ```
    * UserSignOn class is then calls its POST method to check if the user exits by its email
      * if yes, it returns a user already exists message
      * if no, it connects to the database to insert the user to database.
      * Please see screenshots below
    * The screenshot for register screen(for new user):
    ![register screen for new user](../images/002-06-registerscreen.png)
    ---------------------------------------------------------------------------------
    * The screenshot for register screen(if user exists):
    ![register screen if user exists](../images/002-06-registerscreenuserexists.png)
    ---------------------------------------------------------------------------------

  * The ***/login*** screen:
    * The login screen is the ***authentication(default: /auth)*** page
    * Since we have overridden this page to be ***/login*** page via following config:
      * ***flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'***
      * this is done to override '/login' as auth URL instead of the default '/auth'
    * The following payload is passed to ***/login*** resource via ***POST** method to register
      ```
      {
        "email": "Naeemm@futurecloud.com",
        "password": "PassNaeem"
      }
      ```
    * On successful login the JWT token and the id of the user is returned as below:
      ```
      {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTQ2NTM0NDIsImV4cCI6MTU1NDY1NTI0MiwibmJmIjoxNTU0NjUzNDQyLCJpZGVudGl0eSI6MX0.ZL9WsQws-smbxbovGBD1eTwHpe_o6iezA3YLvaNBKpc",
        "user_id": 1
      }
      ```
    * This ***token*** (it will vary each time you login) is copied and passed to ***"Authoriozation"*** jeader as (JWT tokenstring) to all the methods(GET, POST, DELETE, PUT for the Product and Products resource)
    * E.g. ***JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTQ2NTM0NDIsImV4cCI6MTU1NDY1NTI0MiwibmJmIjoxNTU0NjUzNDQyLCJpZGVudGl0eSI6MX0.ZL9WsQws-smbxbovGBD1eTwHpe_o6iezA3YLvaNBKpc***
    * The screenshot for login screen(on success):
    ![login screen on success](../images/002-06-loginscreen.png)
    ---------------------------------------------------------------------------------

    * On failed login the following message can be returned(may vary depending on error):
      ```
      {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTQ2NTM0NDIsImV4cCI6MTU1NDY1NTI0MiwibmJmIjoxNTU0NjUzNDQyLCJpZGVudGl0eSI6MX0.ZL9WsQws-smbxbovGBD1eTwHpe_o6iezA3YLvaNBKpc",
        "user_id": 1
      }
      ```
    * The screenshot for login screen(on failure):
    ![login screen on failure](../images/002-06-loginscreenonfaliure.png)
    ---------------------------------------------------------------------------------
### Updating Security based RESTful API Version 1(The Product and Products Resources):
  * Since we have already covered the User and UserSignOn resources in the above sections and seen how do we register as a new user and login using the sucessfully registered credentials
  * This section now focuses on the ***Product*** and ***Products*** resources.
  * The following two commands in the ***app_v1.py*** sets the two resources:
    ```
    restApi.add_resource(Product,'/product/<string:name>')
    restApi.add_resource(Products,'/products')
    ```
  * ***Product*** and ***Products*** classes are defined in the file - ***productDAL.py***
  * The app code for the ***productDAL.py***
    ```
    import sqlite3
    from flask_restful import Resource, reqparse
    from flask_jwt import jwt_required

    #create a Product model class to represent a Product and its operations
    class Product(Resource):
        dbName= "dbProducts.db"
        tblName= 'tblProducts'

        # define parser
        parser = reqparse.RequestParser()
        parser.add_argument("desc", type=str, required=True, help="Product Description can not be blank.")
        parser.add_argument("price", type=float, required=True, help="Product Price can not be blank.")
        parser.add_argument("qty", type=float, required=True, help="Product Quantity can not be blank.")

        @classmethod
        def getProductByName(cls, name):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()
            selectQuery = "SELECT * FROM {tableName} WHERE name=?".format(tableName=cls.tblName)
            retValue = dbCursor.execute(selectQuery, (name,))
            oneRow = retValue.fetchone()
            if oneRow:
                return {"product" : {'name': oneRow[0], 'desc': oneRow[1], 'price': oneRow[2], 'qty': oneRow[3]}}
            dbConnection.close()

        @classmethod
        def AddProduct(cls, product):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()

            insertQuery = "INSERT INTO {tableName} VALUES(?,?,?,?)".format(tableName=cls.tblName)
            
            dbCursor.execute(insertQuery, (product['name'], product['desc'], product['price'], product['qty']))

            dbConnection.commit()
            dbConnection.close()


        @classmethod
        def UpdateProduct(cls, product):
            dbConnection = sqlite3.connect(cls.dbName)
            dbCursor = dbConnection.cursor()

            updateQuery = "UPDATE {tableName} SET desc=?, price=?, qty=? WHERE name=?".format(tableName=cls.tblName)
            
            dbCursor.execute(updateQuery, (product['desc'], product['price'], product['qty'], product['name']))

            dbConnection.commit()
            dbConnection.close()


        @jwt_required()
        def get(self, name):
            product = self.getProductByName(name)
            if product:
                return product
            else:
                return {"message" : "Product by the name {pname} not found!!!".format(pname=name)}, 404

        @jwt_required()
        def post(self, name):
            # check if the product exists
            if self.getProductByName(name):
                return {"message" : "Product by the name {pname} already exists, select a new name!!!".format(pname=name)}, 400

            # otherwise insert the new product
            data = Product.parser.parse_args()
            desc = data['desc']
            price = data['price']
            qty = data['qty']
            new_product = {'name': name, 'desc': desc, 'price': price, 'qty': qty}
            try:
                Product.AddProduct(new_product)
                returnMessage = "Congrats, Product by the name : {pname} has been ADDED.".format(pname=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 500 
            # return new_product

        @jwt_required()
        def put(self, name):
            product = self.getProductByName(name)

            data = Product.parser.parse_args()
            desc = data['desc']
            price = data['price']
            qty = data['qty']
            updated_product = {'name': name, 'desc': desc, 'price': price, 'qty': qty}

            if product:
                try:
                    Product.UpdateProduct(updated_product) 
                    returnMessage = "Congrats, Product by the name : {pname} has been UPDATED.".format(pname=name)
                    return {"message" : returnMessage }
                except:
                    return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully UPDATED!!!".format(pname=name)}, 500 
            else:
                try:
                    Product.AddProduct(updated_product) 
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
  * The ***Product*** class which represents a Product 
    * first defines a parser:
      * to retrieve product desc, price and quantity
      * and validate if none of these are blank
      ```
      # define parser
      parser = reqparse.RequestParser()
      parser.add_argument("desc", type=str, required=True, help="Product Description can not be blank.")
      parser.add_argument("price", type=float, required=True, help="Product Price can not be blank.")
      parser.add_argument("qty", type=float, required=True, help="Product Quantity can not be blank.")
      ```
      * The screenshot for parser in the Products class:
      ![parser in the Products class](../images/002-06-parserintheProductsclass.png)
      ---------------------------------------------------------------------------------
    
    * then defines 3 ***classmethods*** 
      * ***getProductByName*** function:
        * retrives a product from the tblProducts table by name
        * please see the query below:
        ```
        selectQuery = "SELECT * FROM {tableName} WHERE name=?".format(tableName=cls.tblName)
        retValue = dbCursor.execute(selectQuery, (name,))
        ```
      * ***AddProduct*** function:
        * inserts/adds a product to the tblProducts table
        * please see the query below:
        ```
        insertQuery = "INSERT INTO {tableName} VALUES(?,?,?,?)".format(tableName=cls.tblName)
        dbCursor.execute(insertQuery, (product['name'], product['desc'], product['price'], product['qty']))
        ```
      * ***UpdateProduct*** function:
        * * updates a product to the tblProducts table by name
        * please see the query below:
        ```
        updateQuery = "UPDATE {tableName} SET desc=?, price=?, qty=? WHERE name=?".format(tableName=cls.tblName)
        dbCursor.execute(updateQuery, (product['desc'], product['price'], product['qty'], product['name']))
        ```
      * The screenshot for class methods in the Products class:
      ![class methods in the Products class](../images/002-06-classmethodsintheProductsclass.png)
      ---------------------------------------------------------------------------------

    * then defines a ***CRUD methods(get, post, put, delete)***:
      * The ***get*** method - retrieves a single product by name
      * and validate if none of these are blank
      ```
      @jwt_required()
          def get(self, name):
              product = self.getProductByName(name)
              if product:
                  return product
              else:
                  return {"message" : "Product by the name {pname} not found!!!".format(pname=name)}, 404

      ```
      * The screenshot for ***get*** method appcode in the Products class:
        ![get method in the Products class](../images/002-06-getmethodintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***get*** method in the Products class(on sucess):
        * Please see the success message and the JWT authorization token
        ![get method in the Products class](../images/002-06-getmethodonsuccessintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***get*** method in the Products class(onfailure):
        * E.g. if the product requested does not exist
        ![get method in the Products class](../images/002-06-getmethodonfailureintheProductsclass.png)
        ---------------------------------------------------------------------------------
      
      * The ***post*** method - adds a products to tblProducts table and notifies on success, if product already exists then notfies that product is already existing
      * here is the app code:
      ```
      @jwt_required()
      def post(self, name):
          # check if the product exists
          if self.getProductByName(name):
              return {"message" : "Product by the name {pname} already exists, select a new name!!!".format(pname=name)}, 400

          # otherwise insert the new product
          data = Product.parser.parse_args()
          desc = data['desc']
          price = data['price']
          qty = data['qty']
          new_product = {'name': name, 'desc': desc, 'price': price, 'qty': qty}
          try:
              Product.AddProduct(new_product)
              returnMessage = "Congrats, Product by the name : {pname} has been ADDED.".format(pname=name)
              return {"message" : returnMessage }
          except:
              return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 500 
          # return new_product
      ```
      * The screenshot for ***post*** method appcode in the Products class:
        ![post method in the Products class](../images/002-06-postmethodintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***post*** method in the Products class(on sucess):
        * Please see the success message and the JWT authorization token
        ![post method in the Products class](../images/002-06-postmethodonsuccessintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***post*** method in the Products class(onfailure):
        * E.g. if the product already exists
        ![post method in the Products class](../images/002-06-postmethodonfailureintheProductsclass.png)
        ---------------------------------------------------------------------------------
    
      * The ***put*** method - updates aproduct if exists else inserts a product new
      * and validate if none of these are blank
      ```
      @jwt_required()
      def put(self, name):
          product = self.getProductByName(name)

          data = Product.parser.parse_args()
          desc = data['desc']
          price = data['price']
          qty = data['qty']
          updated_product = {'name': name, 'desc': desc, 'price': price, 'qty': qty}

          if product:
              try:
                  Product.UpdateProduct(updated_product) 
                  returnMessage = "Congrats, Product by the name : {pname} has been UPDATED.".format(pname=name)
                  return {"message" : returnMessage }
              except:
                  return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully UPDATED!!!".format(pname=name)}, 500 
          else:
              try:
                  Product.AddProduct(updated_product) 
                  returnMessage = "Congrats, Product by the name : {pname} has been ADDED.".format(pname=name)
                  return {"message" : returnMessage }
              except:
                  return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 500 
          # return updated_product

      ```
      * The screenshot for ***put*** method appcode in the Products class:
        ![put method in the Products class](../images/002-06-putmethodintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***put*** method in the Products class(on sucess and insert):
        * Please see the success message and the JWT authorization token
        ![put method in the Products class on insert](../images/002-06-putmethodonsuccessinsertintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***put*** method in the Products class(on success and update):
        ![put method in the Products class on update](../images/002-06-putmethodonsuccessupdateintheProductsclass.png)
        ---------------------------------------------------------------------------------

      * The ***delete*** method - deletes a single product by name
        ```
        @jwt_required()
        def delete(self, name):
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()
            deleteQuery = "DELETE FROM {tableName} WHERE name=?".format(tableName=self.tblName)
            dbCursor.execute(deleteQuery, (name,))
            
            dbConnection.commit()
            dbConnection.close()
            return {"message" : "Product by the name {pname} DELETED!!!".format(pname=name)}
        ```
      * The screenshot for ***delete*** method appcode in the Products class:
        ![delete method in the Products class](../images/002-06-deletemethodintheProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***delete*** method in the Products class(on sucess):
        * Please see the success message and the JWT authorization token
        ![delete method in the Products class](../images/002-06-deletemethodonsuccessintheProductsclass.png)
        ---------------------------------------------------------------------------------

  * The ***Products*** class which represents a list of Products
    * defines a get method to retrives a list of all products:
    * The ***get*** method - retriving a list of all products
        ```
        @jwt_required()
        def delete(self, name):
            dbConnection = sqlite3.connect(self.dbName)
            dbCursor = dbConnection.cursor()
            deleteQuery = "DELETE FROM {tableName} WHERE name=?".format(tableName=self.tblName)
            dbCursor.execute(deleteQuery, (name,))
            
            dbConnection.commit()
            dbConnection.close()
            return {"message" : "Product by the name {pname} DELETED!!!".format(pname=name)}
        ```
      * The screenshot for ***get*** method appcode in the Products class:
        ![get method in the Products class](../images/002-06-getmethodinthelisofProductsclass.png)
        ---------------------------------------------------------------------------------
      * The screenshot for ***get*** method in the Products class:
        ![get method in the Products class](../images/002-06-getmethodonsuccessinthelisofProductsclass.png)
        ---------------------------------------------------------------------------------

  * The ***app_v1.py*** class which executes the RESTful API and lets you 
    * ***register***
    * ***login***
    * ***perform CRUD operations on the Product***
    * Import code snippets in the app_v1.py script:
      * importing modules
        * ***from securityutils import checkIdentity, checkAuthenticity*** - securityutils functions for authentication
        * ***from userDAL import UserSignOn*** - custom User DAL
        * ***from productDAL import Product, Products*** - custom Product, Products DAL
      * setting configs
        * ***flaskApp.config['PROPAGATE_EXCEPTIONS'] = True*** # to enforce propagate an exception even if debug is set to false
        * ***flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'***  # to enforce /login as the auth page rather then /auth
        * ***flaskApp.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)*** # to enforce JSON web token expiration to a custom value in seconds. Defaults to 300 seconds(5 minutes)
        * ***flaskApp.config['JWT_AUTH_USERNAME_KEY'] = 'email'*** # to enforce AUTH key as email rather than default username
      * Setting custom response handler
        * to return custom resposne in addition to just the token(here user id also)
        @jwt.auth_response_handler
        ```
        def custom_response_handler(access_token, identity):
            return jsonify({
                                'access_token': access_token.decode('utf-8'),
                                'user_id': identity.id
                          })
        ```
      * adding resources to API
        * ***restApi.add_resource(Product,'/product/<string:name>')*** - handles the Product resource
        * ***restApi.add_resource(Products,'/products')*** - handles the Products resource
        * ***restApi.add_resource(UserSignOn,'/register')***  - handles the registration 
    * The app code for app_v1.py: 
        ```
        from flask import Flask, jsonify
        from flask_restful import Api
        from flask_jwt  import JWT, current_identity
        from datetime import timedelta

        from securityutils import checkIdentity, checkAuthenticity
        from userDAL import UserSignOn
        from productDAL import Product, Products

        flaskApp = Flask(__name__)

        # setting config
        flaskApp.config['PROPAGATE_EXCEPTIONS'] = True # to enforce propagate an exception even if debug is set to false
        flaskApp.config['JWT_AUTH_URL_RULE'] = '/login'  # to enforce /login as the auth page rather then /auth
        flaskApp.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) # to enforce JSON web token expiration to a custom value in seconds. Defaults to 300 seconds(5 minutes)
        flaskApp.config['JWT_AUTH_USERNAME_KEY'] = 'email' # to enforce AUTH key as email rather than default username

        # add a secret key 
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
      * The screenshot for appcode of app_v1.py:
        ![appcode of app_v1.py](../images/002-06-appcode-of-app-v1-py.png)
        ---------------------------------------------------------------------------------
      * The screenshot of the running RESTful API:
        ![screenshot of the running RESTful API ](../images/002-06-screenshotrunningAPI.png)
        ---------------------------------------------------------------------------------