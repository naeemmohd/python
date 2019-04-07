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
  * Upcoming

