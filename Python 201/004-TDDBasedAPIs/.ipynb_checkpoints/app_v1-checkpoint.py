#import Flask class from flask package
from flask import Flask
#import Flask class from flask_restful package - 
# Api represents an API and a Resource represents a resource which will support methods(HTTP verbs)
from flask_restful import Resource, Api

# create a flask app
flaskApp = Flask(__name__)

#create an API 
restApi = Api(flaskApp)

#create a class Student which will represent a resource(will extend from Resource type class)
class Student(Resource):
    #define get method
    def get(self, name):
        return {'student' : name}

# add resource to Api. e.g. http://127.0.0.1:5000/student/Naeem 
restApi.add_resource(Student,'/student/<string:name>' )

# run the app on a specific port
flaskApp.run(port=5050)
