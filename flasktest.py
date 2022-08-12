from flask import Flask, request
from markupsafe import escape
from db import db, Developers 
import json
 


#flask init
app = Flask(__name__)

#DB init and config
db_filename = "session2.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/developers/', methods = ["POST"])
def create_developer():

    body = json.loads(request.data)
    n, l = body.get("nickname"), body.get("lang")

    dev = Developers(nickname = n, lang = l)
    db.session.add(dev)
    db.session.commit()

    return "Created"

@app.route('/developers/', methods = ["GET"])
def get_developers():
    
    res = [dev.serialize() for dev in Developers.query.all()]
    return json.dumps(res) 

    
 


@app.route("/")
def hello_world():
    return "Hello, World! gif welcome to the home page"

#escape to protect user details from injection attacks

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)} !"

#convertor: get specified data type input
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'
 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {subpath}'

@app.route('/projects/')
def projects():
    return "The projects page"