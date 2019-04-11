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



    
    