
from flask import Flask

app = Flask(__name__)

# Decorator
@app.route("/")
def index():
      return "hello world"


app.run(debug = True)