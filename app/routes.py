from app import app
from flask import render_template

# Decorators:
@app.route("/")
@app.route("/index")
def index():
    context = {
        "user": {"username":"Zh"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)



