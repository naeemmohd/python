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