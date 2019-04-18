from app import flaskApp
from dbutils import db

db.init_app(flaskApp)

@flaskApp.before_first_request
def setupDatabase():
    db.create_all()