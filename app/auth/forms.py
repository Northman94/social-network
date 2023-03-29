from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    validators,
    PasswordField
)

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired() ])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=6)])


