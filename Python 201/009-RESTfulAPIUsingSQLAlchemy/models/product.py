from SQLAlchemyDB import sqlAlchemyDb

class ProductModel(sqlAlchemyDb.Model):

    __tablename__= 'tblProducts'

    id = sqlAlchemyDb.Column(sqlAlchemyDb.Integer, primary_key=True)
    name = sqlAlchemyDb.Column(sqlAlchemyDb.String(100))
    desc = sqlAlchemyDb.Column(sqlAlchemyDb.String(100))
    price = sqlAlchemyDb.Column(sqlAlchemyDb.Float(precision=2))
    qty = sqlAlchemyDb.Column(sqlAlchemyDb.Integer)

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
        sqlAlchemyDb.session.add(self)
        sqlAlchemyDb.session.commit()

    def Delete(self):
        sqlAlchemyDb.session.delete(self)
        sqlAlchemyDb.session.commit()