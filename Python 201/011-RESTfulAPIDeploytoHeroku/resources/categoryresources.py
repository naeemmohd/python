from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.categorymodel import CategoryModel

#create a Product model class to represent a Product and its operations
class Category(Resource):

    @jwt_required()
    def get(self, name):
        category = CategoryModel.getCategoryByName(name)
        if category:
            return category.json()
        else:
            return {"message" : "Category by the name {name} not found!!!".format(name=name)}, 404

    @jwt_required()
    def post(self, name):
        # check if the category exists
        if CategoryModel.getCategoryByName(name):
            return {"message" : "Category by the name {name} already exists, select a new name!!!".format(name=name)}, 400

        # otherwise insert the new category
        category = CategoryModel(name)
        try:
            category.Save()
            returnMessage = "Congrats, Category by the name : {name} has been ADDED.".format(name=name)
            return {"message" : returnMessage }
        except:
            return {"message" : "Sorry!!!, The Category by the name {name} could not be sucessfully ADDED!!!".format(name=name)}, 500 
        # return category.json(), 201

    @jwt_required()
    def put(self, name):
        category = CategoryModel.getCategoryByName(name)

        if category:
            try:
                category.name = name
                category.Save()
                returnMessage = "Congrats, Category by the name : {name} has been UPDATED.".format(name=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The Category by the name {name} could not be sucessfully UPDATED!!!".format(name=name)}, 500 
        else:
            try:
                category = CategoryModel(name)
                category.Save()
                returnMessage = "Congrats, Category by the name : {name} has been ADDED.".format(name=name)
                return {"message" : returnMessage }
            except:
                return {"message" : "Sorry!!!, The Category by the name {name} could not be sucessfully ADDED!!!".format(name=name)}, 500 
        
        # return category.json()
        
    @jwt_required()
    def delete(self, name):
        category = CategoryModel.getCategoryByName(name)
        if category:
            category.Delete()
            return {"message" : "Category by the name {name} DELETED!!!".format(name=name)}
        else:
            return {"message" : "Category by the name {name} can not be found!!!".format(name=name)}, 404



#create a Categories model class to represent list of Categories and its operations
class Categories(Resource):
    @jwt_required()
    def get(self):
        # using a map function with lambda
        categories = list(map(lambda category: category.json(), CategoryModel.query.all()))
        # OR using a list comprehensions 
        # categories = [category.json() for category in CategoryModel.query.all()]
        return {"categories" : categories}, 200



    
    