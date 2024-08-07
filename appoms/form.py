from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, PasswordField, RadioField
from wtforms import  SelectField, BooleanField, EmailField
from wtforms.validators import DataRequired, Email


class AppomsForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')
