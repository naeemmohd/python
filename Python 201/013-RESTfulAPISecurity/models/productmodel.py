# import SQLAlchemy object
from dbutils import db

# create the Product model class 
class ProductModel(db.Model):

    # define table name for ORM
    __tablename__= 'tblProducts'

    # define table schema 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    qty = db.Column(db.Integer)

    # define relationships with parent/child table
    category_id = db.Column(db.Integer, db.ForeignKey("tblCategory.id"))
    category = db.relationship("CategoryModel")

    def __init__(self, name, desc, price, qty, category_id):
        self.name= name
        self.desc= desc
        self.price= price
        self.qty= qty
        self.category_id=category_id
    
    def json(self):
        return {'name' : self.name, 'desc' : self.desc, 'price' : self.price, 'qty' : self.qty, 'category_id' : self.category_id}

    @classmethod
    def getProductByName(cls, name):
        return cls.query.filter_by(name=name).first()

    def Save(self):
        db.session.add(self)
        db.session.commit()

    def Delete(self):
        db.session.delete(self)
        db.session.commit()