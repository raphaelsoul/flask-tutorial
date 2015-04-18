from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(Form):
	email = StringField('Email address', [DataRequired(), Email()])
	password = PasswordField('Password', [DataRequired()])

class RegisterForm(Form):
	username = StringField('Username', [DataRequired()])
	email = StringField('Email address', [DataRequired(), Email()])
	password = PasswordField('Password', [DataRequired()])
	confirm = PasswordField('Repeat Password', [DataRequired(),EqualTo('password', message='Passwords must match')])
	accept_tos = BooleanField('I accept the TOS', [DataRequired()])