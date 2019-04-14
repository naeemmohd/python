# import the SQLAlchemy object
from dbutils import db

# create a new class Category class 
# Category and Item Model classes have one to many relationship
# one to many relationship means: 
# - one item can belong to one category only
# - and one category can have zero, one or more items belonging to that category
class CategoryModel(db.Model):
    # define the ORM table
    __tablename__= "tblCategory"

    # define the table schema 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    # ***Cascade*** affect is - all and delete orphan/child record too when deleting parent object 
    # ***lazy=dynamic*** means on the products object is populated then dont call the DB again and again when calling json method
    products = db.relationship("ProductModel", cascade="all, delete-orphan", lazy="dynamic")
    # products = db.relationship('ProductModel', lazy='dynamic')

    # initialize 
    def __init__(self, name):
        self.name=name

    # json representation 
    def json(self):
        return {'name': self.name, 'products': [product.json() for product in self.products.all()]}
    # save a Category
    def Save(self):
        db.session.add(self)
        db.session.commit()

    # delete a Category - 
    def Delete(self):
        db.session.delete(self)
        db.session.commit()

    # search by name 
    @classmethod
    def getCategoryByName(cls, name):
        return cls.query.filter_by(name=name).first()