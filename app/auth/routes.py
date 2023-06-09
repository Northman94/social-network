
from . import bp # from app.auth import bp
from flask import render_template, redirect, flash, url_for, request
from .forms import LoginForm, RegisterForm


@bp.route("/login", methods=["GET", "POST"])
def login():
    # create LoginForm object
    form = LoginForm()

    # validate form on "POST" request
    if form.validate_on_submit():
        flash(f"Submitted username={form.data['username']}, remember={form.data['remember']}", category="success")

        # redirect to home page
        return redirect(url_for("main.index"))
    # render 'login.html' template with passed form
    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    # create LoginForm object
    form = RegisterForm()

    # validate form on "POST" request
    if form.validate_on_submit():
        flash(f"Registered Username={form.data['username']}, Email={form.data['email']}", category="success")

        # redirect to home page
        return redirect(url_for("main.index"))
    return render_template("auth/register.html", form=form)