from flask import Flask
from markupsafe import escape

app = Flask(__name__)

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