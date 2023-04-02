
from app import db
from app.main import bp
from flask import render_template

from app.models import User


@bp.route("/")
@bp.route("/index")
def index():
    users_data = [
        {
            "username": "Zh",
            "email": "Zh@ll.ll"
        },
        {
            "username": "Ton",
            "email": "Ton@ll.ll"
        },
        {
            "username": "De",
            "email": "De@ll.ll"
        },
        {
            "username": "Tan",
            "email": "Tan@ll.ll"
        },
    ]
    for u in users_data:
        user = (
            db.session.query(User)
                .filter(
                User.username == u.get('username'),
                User.email == u.get('email')
            ).first()
        )
        if user:
            continue

        user = User(
            username=u.get('username'),
            email=u.get('email')
        )
        db.session.add(user)
    db.session.commit()

    users_query = db.session.query(User)
    users = users_query.all()
    print(users)
    return render_template("index.html", users=users)


@bp.route("/about")
def about():
    return render_template("about.html")



