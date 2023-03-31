
from app import app
from . import bp
#from auth import bp
from flask import render_template, redirect, url_for
from .registerform import RegisterForm

# Decorators:
@app.route("/")
@app.route("/index")
def index():
    context = {
        "user": {"username":"Zh"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()  # Form Fields

    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("auth/register.html", form=form)

"""
    context = {
        "user": {"username": "Zh"},
        "title": "Regestration"
    }
"""


