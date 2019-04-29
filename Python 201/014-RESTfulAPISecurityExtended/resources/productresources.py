from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity
from models.productmodel import ProductModel

#create a Product model class to represent a Product and its operations
class Product(Resource):

    # define parser
    parser = reqparse.RequestParser()
    parser.add_argument("desc", type=str, required=True, help="Product Description can not be blank.")
    parser.add_argument("price", type=float, required=True, help="Product Price can not be blank.")
    parser.add_argument("qty", type=float, required=True, help="Product Quantity can not be blank.")
    parser.add_argument("category_id", type=int, required=True, help="Product Category Id can not be blank.")

    @jwt_required
    def get(self, name):
        product = ProductModel.getProductByName(name)
        if product:
            return product.json()
        return {"message" : "Product by the name {name} not found!!!".format(name=name)}, 404

    @jwt_required
    def post(self, name):
        # check if the product exists
        if ProductModel.getProductByName(name):
            return {"message" : "Product by the name {name} already exists, select a new name!!!".format(name=name)}, 400

        # otherwise insert the new product
        data = Product.parser.parse_args()
        
        new_product = ProductModel(name, **data)
        try:
            new_product.Save()
            returnMessage = "Congrats, Product by the name : {name} has been ADDED.".format(name=name)
            return {"message" : returnMessage }
        except:
            return {"message" : "Sorry!!!, The product by the name {name} could not be sucessfully ADDED!!!".format(name=name)}, 500 
        # return new_product.json(), 201

    @jwt_required
    def put(self, name):
        product = ProductModel.getProductByName(name)

        data = Product.parser.parse_args()
       
        if product:
            try:
                product.desc= data['desc']
                product.price= data['price']
                product.qty= data['qty']
                product.category_id = data['category_id']
                
                product.Save()
                returnMessage = "Congrats, Product by the name : {name} has been UPDATED.".format(name=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The product by the name {name} could not be sucessfully UPDATED!!!".format(name=name)}, 500 
        else:
            try:
                product = ProductModel(name, **data)
                product.Save()
                returnMessage = "Congrats, Product by the name : {name} has been ADDED.".format(name=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The product by the name {name} could not be sucessfully ADDED!!!".format(name=name)}, 500 
        
        # return product.json()
        
    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims["isadmin"]:
            return {'message' : 'Sorry, you need an administrator priviledge to delete a product.'}
        
        tobedeleted_product = ProductModel.getProductByName(name)
        if tobedeleted_product:
            tobedeleted_product.Delete()
            return {"message" : "Product by the name {name} DELETED!!!".format(name=name)}, 200
        return {"message" : "Product by the name {name} can not be found!!!".format(name=name)}, 404



#create a Products model class to represent list of Products and its operations
class Products(Resource):
    @jwt_optional
    def get(self):
        # using a map function with lambda
        # products = list(map(lambda product: product.json(), ProductModel.query.all()))
        userid = get_jwt_identity()
        products = list([x.json() for x in ProductModel.getAll()])
        if userid:
            return {
                "products" : products
            }, 200
        products = list([x.name for x in ProductModel.getAll()])
        return {
            "products" : products,
            "message" : "Detailed info only after you login."
        }, 200



    
    