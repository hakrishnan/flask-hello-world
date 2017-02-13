# ----------- FLASK HELLO WORLD ----------------#

# import flask class from flask package
from flask import Flask

# create an application object
app = Flask(__name__)

# use the decorator function to the link the view function to a URL
@app.route("/")
@app.route("/hello")

#define a view using a function to return a string
def hello_world():
    return "Hello, World!"

# start the development server using the run() method
if __name__=="__main__":
    app.run()
