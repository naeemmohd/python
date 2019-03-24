# create a file app.py using command in termimal window - nano app.py

# import Flask module from the flask package
from flask import Flask

# create an app from the Flask module
flaskApp = Flask(__name__)

# create a decorator to refer to the home page(/) of the application
# and define the function to be called if the home page is requested
@flaskApp.route('/')
def flaskHome():
    return "Welcome to your first Flask Home page"

# run the app on a specific port
flaskApp.run(port=5000)

# Execute this file in the terminal window using command - python app.py
# and watch the output for the website endpoint
