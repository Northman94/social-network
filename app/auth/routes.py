
from . import bp
from flask import render_template, redirect, url_for
from .form import LoginForm, RegisterForm


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm() #Form Fields

    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()  # Form Fields

    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("auth/register.html", form=form)