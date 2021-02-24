from flask_wtf import FlaskForm
import email_validator
from wtforms import validators, StringField,PasswordField,SubmitField
from wtforms.validators import ValidationError, DataRequired,Email,EqualTo,Length

class RegistrationForm(FlaskForm):
    names = StringField('Full names', validators=[DataRequired(message="You left this empty")])
    email = StringField('Email', validators=[DataRequired(message="This must be filled"), Email(message="Not a valid email")])
    password = PasswordField('Password', validators=[Length(min=8, message="Your password should be at least 8 characters"), DataRequired(message=" You need to fill this field")])
    confirm_password = PasswordField(validators=[EqualTo('password', message="passwords must match")])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired(),Email(message="This email is invalid ")])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Login')