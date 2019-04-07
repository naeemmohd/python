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
            return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 400 
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
                return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully UPDATED!!!".format(pname=name)}, 400 
        else:
            try:
                Product.AddProduct(updated_product) 
                returnMessage = "Congrats, Product by the name : {pname} has been ADDED.".format(pname=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The product by the name {pname} could not be sucessfully ADDED!!!".format(pname=name)}, 400 
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



    
    