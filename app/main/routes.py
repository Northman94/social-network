
from app import app
from flask import render_template, redirect, url_for


# Decorators:
@app.route("/")
@app.route("/index")
def index():
    context = {
        "user": {"username":"Zh"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)

@app.route("/about")
def about():
    return render_template("about.html")



"""
    context = {
        "user": {"username": "Zh"},
        "title": "Regestration"
    }
"""


