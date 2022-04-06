from flask import Flask

#this is an instance of the flask class 
#__name__ is a module 
app = Flask(__name__)

#route is a decorator which tells flask info on URL 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#debug mode can be used to see edits made to web server without having to restart server