from . import bp

@bp.route("/")
def index():
    return "Hello from auth"

@bp.route("/login")
def login():
    return "Hello from Login"