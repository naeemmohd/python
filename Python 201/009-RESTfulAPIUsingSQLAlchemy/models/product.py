from SQLAlchemyDB import db

class ProductModel(db.Model):

    __tablename__= 'tblProducts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    qty = db.Column(db.Integer)

    def __init__(self, name, desc, price, qty):
        self.name= name
        self.desc= desc
        self.price= price
        self.qty= qty
    
    def json(self):
        return {'name' : self.name, 'desc' : self.desc, 'price' : self.price, 'qty' : self.qty}

    @classmethod
    def getProductByName(cls, name):
        return cls.query.filter_by(name=name).first()

    def Save(self):
        db.session.add(self)
        db.session.commit()

    def Delete(self):
        db.session.delete(self)
        db.session.commit()