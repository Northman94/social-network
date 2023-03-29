from . import bp
from flask import render_template

@bp.route("/")
def index():
    return "Hello from auth"

@bp.route("/login")
def login():
    return render_template("auth/login.html", form)