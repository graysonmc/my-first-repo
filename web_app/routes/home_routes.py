# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")
    #return "Welcome Home"

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")
    #return "About Me"

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")

    # if the request contains url params, for example a request to "/hello?name=Harper",
    # the request object's args property will hold the values in a dictionary-like structure
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    name = url_params.get("name") or "World" # get the value of "name" from the url params, or use some specified default value

    # INFO: we'll eventually use html templates, but as an interim step to get the outputs right first, we'll use string interpolation:
    message = f"Hello, {name}!"
    return render_template("hello.html", message=message, x=5, y=20)
    #return message