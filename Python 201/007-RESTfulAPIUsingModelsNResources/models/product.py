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