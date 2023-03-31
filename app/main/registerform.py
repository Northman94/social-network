from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    validators,
    EmailField,
    PasswordField,
    SubmitField
)

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired() ])
    email = EmailField("Email", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=6)])
    submit = SubmitField("Register")
